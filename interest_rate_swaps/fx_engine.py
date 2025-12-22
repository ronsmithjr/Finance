'''
Handles FX rates and conversions
'''

def convert_currency(amount: float, fx_rate: float, direction: str="base_to_quote") -> float:
    return amount * fx_rate if direction == "base_to_quote" else amount / fx_rate