'''
Handles fixed rate calculation and overall swap valuation.
'''

def calculate_fixed_rate(discount_factors: list) -> float:
    numerator = 1 - discount_factors[-1]
    denominator = sum(discount_factors)
    return numerator / denominator

def value_swap(fixed_leg: float, floating_leg: float) -> float:
    return fixed_leg - floating_leg