

'''
Generates disocunt factors from input yield curve.
Both of these are the same functions.  They are just written differently

SIMPLE INTEREST DISCOUNT FACTOR FORMULA
Discount Factor = 1 / (1 + r * t)

COMPOUND INTEREST DISCOUNT FACTOR FORMULA
Discount Factor = 1 / (1 + r) ** t

Discount factors are used to:

Price bonds and swaps
Value future cash flows in investment analysis
Construct yield curves

'''





def build_simple_interest_discount_curve(rates: list, tenors: list) -> list:
    discount_factors = []
    print("Discount Factors:")
    for r, t in zip(rates, tenors):
        discount_factor = 1 / (1 + r * t)
        discount_factors.append(discount_factor)
        print(f"{discount_factor}")
    return discount_factors

def build_simple_interest_discount_curve_1(rates: list, tenors: list) -> list:
    return [1 / (1 + r * t) for r, t in zip(rates, tenors)]


def build_compound_interest_discount_curve(rates: list, tenors: list) -> list:
    discount_factors = []
    print("Discount Factors")
    for r, t in zip(rates, tenors):
        discount_factor = 1 / (1 + r) ** t
        discount_factors.append(discount_factor)
        print(f"{discount_factor}")
    return discount_factors

def build_compund_interest_discount_curve(rates: list, tenors: list) -> list:
    return [1 / (1 + r) ** t for r, t in zip(rates, tenors)]