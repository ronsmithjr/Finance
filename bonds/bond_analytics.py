import numpy as np
import pandas as pd
from datetime import datetime

def bond_panel(coupon, maturity, ytm, freq=2, face=100):
    """
    Bloomberg-style analytics panel:
    Price, YTM, Macaulay Duration, Modified Duration, Convexity,
    and price changes for ±25/50/100 bps.
    """

    # --- Cash flow schedule ---
    periods = int(maturity * freq)
    dt = 1 / freq
    times = np.array([dt * (i + 1) for i in range(periods)])
    cashflows = np.full(periods, coupon * face / freq)
    cashflows[-1] += face  # add principal

    # --- Discount factors ---
    df = 1 / (1 + ytm / freq) ** (np.arange(1, periods + 1))

    # --- Price ---
    price = np.sum(cashflows * df)

    # --- Macaulay Duration ---
    pv_times = times * cashflows * df
    macaulay = np.sum(pv_times) / price

    # --- Modified Duration ---
    modified = macaulay / (1 + ytm / freq)

    # --- Convexity ---
    convexity = np.sum(cashflows * df * times * (times + dt)) / (price * (1 + ytm / freq)**2)

    # --- Repricing for shocks ---
    shocks = np.array([-0.01, -0.005, -0.0025, 0.0025, 0.005, 0.01])
    shock_labels = ["-100 bp", "-50 bp", "-25 bp", "+25 bp", "+50 bp", "+100 bp"]
    prices_shocked = []

    for s in shocks:
        y_new = ytm + s
        df_new = 1 / (1 + y_new / freq) ** (np.arange(1, periods + 1))
        prices_shocked.append(np.sum(cashflows * df_new))

    bond_metadata = []

    bond_metadata.append({
        "Price (Full)"        : f"{price:,.2f}",
        "YTM"                 :f"{ytm*100:,.3f}",
        "Macaulay Duration (years)"   : f"{macaulay:10.4f}",
        "Modified Duration"   : f"{modified:10.4f}",
        "Convexity"           : f"{convexity:10.4f}"
    })
    bond_meta_df = pd.DataFrame(bond_metadata)
    bond_meta_df_pivoted = bond_meta_df.T.reset_index()
    bond_meta_df_pivoted.columns = ['Field','Value']

    # print(bond_meta_df_pivoted)
    shock_data = []
    # --- Print panel ---
    # print("\n" + "="*60)
    # print("               BLOOMBERG-STYLE BOND ANALYTICS")
    # print("="*60)
    # print(f"Price (Full)        : {price:10.4f}")
    # print(f"YTM                 : {ytm*100:10.3f}%")
    # print(f"Macaulay Duration   : {macaulay:10.4f} years")
    # print(f"Modified Duration   : {modified:10.4f}")
    # print(f"Convexity           : {convexity:10.4f}")
    # print("-"*60)
    # print("  Shock     Repriced Price")
    # print("-"*60)
    for lbl, p in zip(shock_labels, prices_shocked):
       # print(f"{lbl:>7}   : {p:10.4f}")
        shock_data.append({
            f"{lbl:>7}": f"{p:10.4f}"
        })

    flat_shock_data = []
    for d in shock_data:
        for k, v in d.items():
            flat_shock_data.append({'Shock': k, 'Repriced Price': v})

    # Create DataFrame
    shock_table = pd.DataFrame(flat_shock_data)
    # print(shock_table)
    # print("="*60 + "\n")
    # print(shock_data)
    # shock_data_df = pd.DataFrame(shock_data)
    #print(shock_data_df)
    # shock_data_pivoted = shock_data_df.T.reset_index()
    # shock_data_pivoted.columns = ['Field','Value']
    # shock_data_melted = shock_data_df.melt(var_name='Field', value_name='Value')
    # print(shock_data_melted)
    # meta_data_full = pd.concat([bond_meta_df_pivoted, shock_table])
    # print(meta_data_full)

    return bond_meta_df_pivoted, shock_table

def save_cashflows_to_csv(meta_df, df, filename):
    with open(filename, 'w', newline='') as f:
        meta_df.to_csv(f, index=False, header=False)
        f.write('\n')
        df.to_csv(f, index=False)

if __name__ == "__main__":
    meta_data, shock_data  = bond_panel(
    coupon=0.04,   # 4% annual coupon
    maturity=10,    # 10 years
    ytm=0.04,      # 4% yield
    freq=2         # semiannual
)
    print("\n" + "="*60)
    print("               BLOOMBERG-STYLE BOND ANALYTICS")
    print("="*60)
    print(meta_data)
    print("-"*60)
    print(shock_data)
    print("="*60 + "\n")

    now_str = datetime.now().strftime("%Y%m%d_%H%M%S")   
    file_name = fr"S:\Finance\assets\meta_bond_datacash_flows_{now_str}.csv"  
    save_cashflows_to_csv(meta_data, shock_data, file_name)
