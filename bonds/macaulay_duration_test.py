import numpy as np

def calculate_macaulay_duration(cash_flows, annual_yield, periods_per_year, bond_price):
    """
    Calculates the Macaulay Duration of a bond.

    Parameters:
    cash_flows (list or array): A list/array of periodic cash flows (coupon payments + face value at maturity).
    annual_yield (float): The bond's annual yield to maturity (as a decimal, e.g., 0.05 for 5%).
    periods_per_year (int): The number of coupon payments per year (e.g., 1 for annual, 2 for semi-annual).
    bond_price (float): The current market price of the bond.

    Returns:
    float: The Macaulay Duration in years.
    """
    periodic_yield = annual_yield / periods_per_year
    total_periods = len(cash_flows)
    
    # Calculate the sum of (time * PV of each cash flow)
    weighted_pv_sum = 0
    for t, cf in enumerate(cash_flows, 1):
        weighted_pv_sum += t * cf / (1 + periodic_yield)**t

    # Macaulay duration in periods
    macaulay_duration_periods = weighted_pv_sum / bond_price

    # Convert to years
    macaulay_duration_years = macaulay_duration_periods / periods_per_year
    
    return macaulay_duration_years

# --- Example Usage ---
# Example: A 3-year bond with a 4% annual coupon, semi-annual payments, 
# $1000 face value, and a 4% annual yield (price at par).

# Inputs:
# Annual coupon payment is 4% of $1000 = $40. Semi-annual payment is $20.
# The final cash flow includes the last coupon payment and the face value ($20 + $1000 = $1020).
example_cash_flows = [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 1020.0] 
example_annual_yield = 0.04 # 4% as a decimal
example_periods_per_year = 2 # Semi-annual payments
example_bond_price = 1000.0 # Price at par since coupon rate equals yield

# Calculate duration
duration = calculate_macaulay_duration(example_cash_flows, example_annual_yield, example_periods_per_year, example_bond_price)

print(f"The Macaulay Duration of the bond is: {duration:.4f} years")

