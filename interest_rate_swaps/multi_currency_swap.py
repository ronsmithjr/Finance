'''
Wraps valuation logic across two currencies

'''
from fx_engine import convert_currency

def value_multi_currency_swap(
        notional_base: float,
        notional_quote: float,
        fixed_rate_base: float,
        floating_rate_quote: float,
        discount_base: list,
        discount_quote: list,
        fx_rate: float,
        basis_spread: float = 0.0

) -> float:
    pv_fixed = notional_base * fixed_rate_base * sum(discount_base)
    pv_float = notional_quote * (floating_rate_quote + basis_spread) * sum(discount_quote)
    pv_float_converted = convert_currency(pv_float, fx_rate, direction="quote_to_base")
    return pv_fixed - pv_float_converted
