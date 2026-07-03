def calculate_car_payment(principal: float, annual_rate: float, years: int) -> dict:
    """
    Calculates the monthly car payment, total payment, and total interest for a car loan.

    Args:
        principal (float): The loan amount (car price minus down payment).
        annual_rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%).
        years (int): The loan term in years.

    Returns:
        dict: A dictionary containing:
            - "Monthly Payment": The monthly payment amount, rounded to 2 decimal places.
            - "Total Payment": The total amount paid over the loan, rounded to 2 decimal places.
            - "Total Interest": The total interest paid, rounded to 2 decimal places.
    """
    n = years * 12
    monthly_rate = annual_rate / 12
    if monthly_rate == 0:
        monthly_payment = principal / n
    else:
        monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** n) / ((1 + monthly_rate) ** n - 1)
    total_payment = monthly_payment * n
    total_interest = total_payment - principal
    return {
        "Monthly Payment": round(monthly_payment, 2),
        "Total Payment": round(total_payment, 2),
        "Total Interest": round(total_interest, 2)
    }

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Car Payment Calculator")
    parser.add_argument('--financed_amount', type=float, default=25000, help='Car price minus down payment (default: 25000)')
    parser.add_argument('--annual_rate', type=float, default=0.06, help='Annual interest rate as decimal (default: 0.06 for 6%)')
    parser.add_argument('--years', type=int, default=5, help='Loan term in years (default: 5)')
    args = parser.parse_args()

    result = calculate_car_payment(args.financed_amount, args.annual_rate, args.years)
    print(f"Monthly Payment: {result['Monthly Payment']}")
    print(f"Total Payment: {result['Total Payment']}")
    print(f"Total Interest: {result['Total Interest']}")
