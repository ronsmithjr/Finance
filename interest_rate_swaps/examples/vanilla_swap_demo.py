from calculators.interest_rate_swap.swap_calculator import calculate_fixed_rate, value_swap
from calculators.interest_rate_swap.discount_curve import build_simple_interest_discount_curve
from calculators.interest_rate_swap.cashflow_engine import net_cashflow

# Sample Input
rates = [0.03, 0.032, 0.035]
tenors = [1, 2, 3]
discounts = build_simple_interest_discount_curve(rates, tenors)
fixed_rate = calculate_fixed_rate(discounts)

# Simulate Cashflows
cf = net_cashflow(0.5, fixed_rate, 0.031, receive_fixed=True)
swap_value = value_swap(fixed_rate * sum(discounts), 1.0) # Floating leg at par

print(f"Fixed Rate: {fixed_rate:.4f}, Net CF: {cf:.4f}, Swap Value: {swap_value:.4f}")