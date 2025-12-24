"""
Core mortgage math (single loan)
PSA = Standard Prepayment Model
CPR = Conditional Prepayment Rate 
SMM = Single Monthly Mortatlity Rate
"""


import numpy as np
import pandas as pd
from tranch import Tranche


def level_payment_mortgage(principal, annual_rate, term_months):
    """Core Mortgage Math"""
    i = annual_rate / 12
    M = principal * (i / 1 - (1 + i) ** (-term_months))
    return M

def psa_cpr(month, psa=100):
    """Return annual CPR for a given month and PSA multiple."""
    base = 0.002 * month if month <= 30 else 0.06 #100%PSA
    return base * (psa / 100.00)

def cpr_to_smm(cpr):
    """Convert annual CPR to monthly SMM"""
    return 1 - (1 - cpr) ** (1/12)

def mortgage_pool_cashflows(
        principal,
        annual_rate,
        term_months,
        psa = 100
):
    M = level_payment_mortgage(principal, annual_rate, term_months)

    records = []
    balance = principal

    for t in range(1, term_months + 1):
        if balance <= 1e-8: #all paied off
            break

        #Scheduled interest and principal
        interest_scheduled = balance * (annual_rate / 12)
        principal_scheduled = M - interest_scheduled

        #CPR and SMM this month
        cpr_t = psa_cpr(t, psa=psa)
        smm_t = cpr_to_smm(cpr_t)


        #Prepayment is applied on balance after scheduled principal
        balance_after_sched = balance -principal_scheduled
        prepayment = balance_after_sched * smm_t

        total_principal = principal_scheduled + prepayment
        total_cash = interest_scheduled + total_principal

        end_balance = balance - total_principal

        records.append({
            "month": t,
            "begin_balance": balance,
            "sched_principal":principal_scheduled,
            "prepayment": prepayment,
            "total_principal": total_principal,
            "interest": interest_scheduled,
            "total_cash": total_cash,
            "end_balance": end_balance,
            "CPR": cpr_t,
            "SMM": smm_t
        })

        balance = end_balance
    return pd.DataFrame(records)

# Write DataFrame to CSV file
def save_cashflows_to_csv(df, filename):
    """Save the mortgage cashflows DataFrame to a CSV file."""
    df.to_csv(filename, index=False)


def build_sequential_cmo(
    pool_cf: pd.DataFrame,
    tranche_notional: list,
    coupon: float
):
    """
    tranche_notional: list of (name, balance) in priority order
    """
    tranches = [Tranche(name, bal, coupon) for name, bal in tranche_notional]
    # for tr in tranches: 
    #     print(tr.name, tr.balance, tr.coupon)
    for _, row in pool_cf.iterrows():
        month = int(row["month"])
        pool_principal = row["total_principal"]
        pool_interest = row["interest"]
        
        # Interest allocation: proportional to balance, same coupon
        total_balance = sum(tr.balance for tr in tranches)
        if total_balance <= 1e-8:
            break  # all paid off
        
        # Principal priority: first tranche, then next, etc.
        remaining_principal = pool_principal
        
        # First compute interest due to each tranche
        tranche_interest = {
            tr.name: tr.balance * (coupon / 12)
            for tr in tranches
        }
        
        # Allocate principal in sequence
        for tr in tranches:
            if remaining_principal <= 1e-10 or tr.balance <= 1e-8:
                continue
            principal_to_tranche = min(remaining_principal, tr.balance)
            remaining_principal -= principal_to_tranche
            tr.add_cashflow(
                month=month,
                interest=tranche_interest[tr.name],
                principal=principal_to_tranche
            )
        
        # If any principal left after all tranches (shouldn’t happen if totals match),
        # it’s effectively unused in this simple model.
    
    return {tr.name: tr.to_frame() for tr in tranches}

def tranche_wal(cf: pd.DataFrame, original_balance: float):
    if cf.empty:
        return 0.0
    principal = cf["principal"].values
    months = cf["month"].values
    wal_years = np.sum((principal / original_balance) * (months / 12.0))
    return wal_years


if __name__ == "__main__":
    pool_principal = 100_000_000
    pool_coupon = .05
    term = 360
    psa = 150

    pool_cf = mortgage_pool_cashflows(
        pool_principal, 
        pool_coupon, 
        term,
        psa)
    
    print(pool_cf.head())
    tranches = [
        ("A",40000000),
        ("B",30000000),
        ("C",30000000)
    ]

    cmo_cfs = build_sequential_cmo(
        pool_cf,
        tranches,
        pool_coupon
    )
    
    for name, df in cmo_cfs.items():
        print(" ")
        # print(f"Total Principal: {pool_cf["total_principal"].sum()}")
        #print(pool_cf["total_principal"].head())
        #print([tr.balance for tr in tranches])


        #print(pool_cf[["month","total_principal"]].head(12))
        #print(f"Name: {name} -> DataFrame {df.head(5)}")
        # print(f"\nTranche {name} summary:")
        # print(df.head())
        # print(df.tail())
    # print(f"Payment {df}")
    # Save to CSV
    # file_name = r"S:\Finance\mortgages\OutputFiles\mortgage_cashflows.csv"
    # save_cashflows_to_csv(df, file_name)
    # print(f"Finished Writing File: {file_name}")