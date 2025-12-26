from datetime import datetime, timedelta
import pandas as pd

def calculate_wal(face_value, coupon_rate, years, payments_per_year, issue_date):
    coupon_payment = face_value * coupon_rate / payments_per_year
    total_payments = years * payments_per_year

    issue_dt = datetime.strptime(issue_date, "%Y-%m-%d")
    payment_dates = [
        issue_dt.replace(year=issue_dt.year + (i // payments_per_year)) +
        timedelta(days=182 * (i % payments_per_year))
        for i in range(1, total_payments + 1)
    ]

    total_weighted_time = 0
    total_cash_flow = 0
    for i in range(1, total_payments + 1):
        time = i / payments_per_year
        if i < total_payments:
            cash_flow = coupon_payment
        else:
            cash_flow = coupon_payment + face_value
        total_weighted_time += time * cash_flow
        total_cash_flow += cash_flow

    wal = total_weighted_time / total_cash_flow
    return wal


def calculate_weighted_average_life(cash_flows, payments_per_year):
    """
    Calculate Weighted Average Life (WAL) from a list of cash flow dicts.
    Assumes 'Period' and 'Cash Flow' keys exist in each dict.
    """
    # Exclude summary row if present
    flows = [cf for cf in cash_flows if isinstance(cf.get("Period", None), int)]
    total_principal = sum(cf["Cash Flow"] for cf in flows if cf["Period"] == flows[-1]["Period"])
    if total_principal == 0:
        total_principal = sum(cf["Cash Flow"] for cf in flows)  # fallback

    weighted_sum = sum(cf["Period"] * cf["Cash Flow"] for cf in flows)
    wal_periods = weighted_sum / total_principal if total_principal else 0
    wal_years = wal_periods / payments_per_year
    return wal_years

def prepare_wal_df(wal):
    wal_data = [{"Weighted Average Life": f"{wal:.2f}"}]
    wal_df = pd.DataFrame(wal_data)
    wal_df_pivoted = wal_df.T.reset_index()
    wal_df_pivoted.columns = ['Field', 'Value']
    return wal_df_pivoted

if __name__ == "__main__":
    # Example usage:
    wal = calculate_wal(1000, 0.04, 10, 2, "2025-10-15")
    print(f"Weighted Average Life (WAL): {wal:.2f} years")
