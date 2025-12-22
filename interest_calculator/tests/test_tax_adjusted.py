from calculators.tax_adjusted import *

def test_calculate_real_after_tax_interest():
    # Scenario 1: Moderate rates
    nominal_rate = 0.06       # 6% nominal interest
    tax_rate = 0.25           # 25% tax
    inflation_rate = 0.03     # 3% inflation
    result = calculate_real_after_tax_interest(nominal_rate, tax_rate, inflation_rate)
    print(f"Scenario 1 - Real after-tax interest: {result:.4f}")  # Expected ≈ 0.0223

    # Scenario 2: High inflation
    nominal_rate = 0.08
    tax_rate = 0.30
    inflation_rate = 0.06
    result = calculate_real_after_tax_interest(nominal_rate, tax_rate, inflation_rate)
    print(f"Scenario 2 - Real after-tax interest: {result:.4f}")  # Expected ≈ 0.0085

    # Scenario 3: Zero inflation
    nominal_rate = 0.05
    tax_rate = 0.20
    inflation_rate = 0.00
    result = calculate_real_after_tax_interest(nominal_rate, tax_rate, inflation_rate)
    print(f"Scenario 3 - Real after-tax interest: {result:.4f}")  # Expected ≈ 0.0400

    # Scenario 4: Zero nominal rate
    nominal_rate = 0.00
    tax_rate = 0.30
    inflation_rate = 0.02
    result = calculate_real_after_tax_interest(nominal_rate, tax_rate, inflation_rate)
    print(f"Scenario 4 - Real after-tax interest: {result:.4f}")  # Expected ≈ -0.0196

test_calculate_real_after_tax_interest()
