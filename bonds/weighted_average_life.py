from datetime import datetime, timedelta

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

if __name__ == "__main__":
    # Example usage:
    wal = calculate_wal(1000, 0.04, 10, 2, "2025-10-15")
    print(f"Weighted Average Life (WAL): {wal:.2f} years")
