def calculate_tax_adjusted_income(income: float, tax_interest_rate: float):
    """
    Calculates the tax-adjusted income after applying a tax interest rate.

    Args:
        income (float): The original income amount before tax.
        tax_interest_rate (float): The tax rate to apply, as a decimal between 0 and 1 (inclusive).

    Returns:
        float: The income amount after tax has been deducted.

    Raises:
        ValueError: If tax_interest_rate is not between 0 and 1 (inclusive).
    """
    if not (0 <= tax_interest_rate <= 1):
        raise ValueError("Tax rate must be between 0 and 1")
    return income * (1 - tax_interest_rate)

def calculate_real_after_tax_interest(nominal_rate: float, tax_rate:float, inflation_rate: float) -> float:
    """
    Calculates the real after-tax interest rate, adjusted for inflation.
    This function computes the effective interest rate after accounting for taxes and inflation.
    It first adjusts the nominal interest rate for taxes, then adjusts the result for inflation
    using the Fisher equation.
    Args:
        nominal_rate (float): The nominal (pre-tax, pre-inflation) interest rate as a decimal (e.g., 0.05 for 5%). Quoted from the lender.
        tax_rate (float): The tax rate applied to the nominal interest, as a decimal (e.g., 0.3 for 30%).
        inflation_rate (float): The inflation rate as a decimal (e.g., 0.02 for 2%).
    Returns:
        float: The real after-tax interest rate, adjusted for inflation.
    Raises:
        ValueError: If any of the input rates are not between 0 and 1 (inclusive).
    """
    if not (0 <= tax_rate <=1) or not (0 <= nominal_rate <=1) or not (0 <= inflation_rate <= 1):
        raise ValueError("Tax / Nominal / inflation  rate must be between 0 and 1")
    
    after_tax_rate = nominal_rate * (1 - tax_rate)
    real_rate = (1 + after_tax_rate) / (1 + inflation_rate) - 1
    return real_rate