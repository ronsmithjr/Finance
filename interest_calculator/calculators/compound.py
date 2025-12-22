def calculate_compound_interest(principal, rate, time, n=1)-> dict:
    """
    Calculate compound interest for a given principal, rate, time, and compounding frequency.

    Args:
        principal (float): The initial amount of money invested or loaned.
        rate (float): The annual interest rate (as a decimal, e.g., 0.05 for 5%).
        time (float): The time the money is invested or borrowed for, in years.
        n (int, optional): The number of times that interest is compounded per year. Defaults to 1.

    Returns:
        dict: A dictionary containing:
            - "Principal": The original principal amount (rounded to 2 decimals).
            - "Rate (%)": The annual interest rate as a percentage (rounded to 2 decimals).
            - "Time (years)": The time period in years.
            - "Compounds / Year": The number of compounding periods per year.
            - "Interest": The interest earned (rounded to 2 decimals).
            - "Total Amount": The total amount after interest (rounded to 2 decimals).
    """
    amount = principal * (1 + rate / n) ** (n * time)
    interest = amount - principal
    return {
        "Interest": round(interest, 2),
        "Total Amount": round(amount, 2)
    }