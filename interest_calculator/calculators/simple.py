def calculate_simple_interest(principal: float, rate: float, time: int) -> dict:
    """
    Calculates simple interest and returns a summary of the calculation.

    Args:
        principal (float): The initial amount of money.
        rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%).
        time (int): The time period in years.

    Returns:
        dict: A dictionary containing:
            - "Principal": The principal amount, rounded to 2 decimal places.
            - "Rate (%)": The interest rate as a percentage, rounded to 2 decimal places.
            - "Time (years)": The time period in years.
            - "Interest": The calculated interest, rounded to 2 decimal places.
            - "Total Amount": The total amount after interest, rounded to 2 decimal places.
    """
    interest = principal * rate * time
    total = principal + interest
    payment = total / time if time else 0
    return {
        "Interest": round(interest, 2),
        "Total Amount": round(total, 2),
        "Payment": round(payment, 2)
    }

if __name__ == "__main__":
    principal = 1000  # Example principal
    rate = 0.05       # Example rate (5%)
    time = 3          # Example time (3 years)
    result = calculate_simple_interest(principal, rate, time)
    interest = result["Interest"]
    total_amount = result["Total Amount"]
    payment = result["Payment"] / 36
    print(f"Interest: {interest}")
    print(f"Total Amount: {total_amount}")
    print(f"Payment: {payment}")