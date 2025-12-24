from datetime import datetime, timedelta

def generate_treasury_cash_flows(face_value=1000, coupon_rate=0.04, years=10, payments_per_year=2, issue_date="2025-10-15"):
    """
    Calculate cash flows for a Treasury bond.
    
    Parameters:
        face_value (float): Principal amount of the bond.
        coupon_rate (float): Annual interest rate (e.g., 0.04 for 4%).
        years (int): Bond maturity in years.
        payments_per_year (int): Number of coupon payments per year.
        issue_date (str): Start date in YYYY-MM-DD format.
    
    Returns:
        List of tuples: (payment_date, cash_flow)
    """
    cash_flows = []
    coupon_payment = face_value * coupon_rate / payments_per_year
    total_payments = years * payments_per_year
    start_date = datetime.strptime(issue_date, "%Y-%m-%d")

    for i in range(1, total_payments + 1):
        payment_date = start_date + timedelta(days=365.25 / payments_per_year * i)
        cash_flow = coupon_payment
        if i == total_payments:
            cash_flow += face_value  # Add principal at maturity
        cash_flows.append((payment_date.date(), round(cash_flow, 2)))

    return cash_flows, start_date.date(), cash_flows[-1][0]  # Also return settlement and maturity dates

if __name__ == "__main__":
    # Example usage
    cash_flows, settlement_date, maturity_date = generate_treasury_cash_flows()
    for date, amount in cash_flows:
        print(f"Payment Date: {date}, Cash Flow: ${amount}")

    print(f"Settlement Date: {settlement_date}")
    print(f"Maturity Date: {maturity_date}")
