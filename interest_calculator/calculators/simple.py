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
    return {
        "Interest": round(interest, 2),
        "Total Amount": round(total, 2)
    }