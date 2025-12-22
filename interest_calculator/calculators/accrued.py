def calculate_accrued_interest(principal: float, annual_rate: float, days_accrued: float, year_basis: int =365) -> float:
    """
    Calculates the accrued interest on a principal amount over a specified number of days.

    Args:
        principal (float): The initial amount of money on which interest is calculated.
        annual_rate (float): The annual interest rate as a percentage (e.g., 5 for 5%).
        days_accrued (float): The number of days for which interest has accrued.
        year_basis (int, optional): The number of days in a year for interest calculation. Defaults to 365.

    Returns:
        dict: A dictionary containing:
            - "Principal": The principal amount, rounded to 2 decimal places.
            - "Rate": The annual rate as a decimal, rounded to 2 decimal places.
            - "Accrued Interest": The calculated accrued interest, rounded to 2 decimal places.
    """
    rate_decimal = annual_rate / 100
    accrued_interest = rate_decimal / year_basis * days_accrued * principal
    return round(accrued_interest, 2)