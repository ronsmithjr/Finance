# calculator/logic.py

from decimal import Decimal, getcontext
import math
from typing import Union

def compound_interest(principal: float, rate: float, years: float) -> float:
    """Calculates compound interest."""
    return principal * (1 + rate) ** years

def compound_interest2(principal: Union[float, Decimal],
                      rate: Union[float, Decimal],
                      years: float,
                      periods_per_year: int = 1,
                      use_decimal: bool = False) -> Union[float, Decimal]:
    """Calculates compound interest. rate is a decimal (e.g. 0.05). 
    periods_per_year=1 means annual compounding. Set use_decimal=True for Decimal math."""
    if use_decimal:
        getcontext().prec = 28
        P = Decimal(principal)
        r = Decimal(rate)
        n = Decimal(periods_per_year)
        return (P * ( (Decimal(1) + r / n) ** (n * Decimal(years)) )).quantize(Decimal('0.01'))
    else:
        return principal * (1 + rate / periods_per_year) ** (periods_per_year * years)

def real_after_tax_rate(nominal_rate: float, tax_rate: float, inflation_rate: float) -> float:
    """Calculates real after-tax interest rate."""
    return (1 + nominal_rate * (1 - tax_rate)) / (1 + inflation_rate) - 1


def simple_interest(principal: float, rate: float, years: float) -> float:
    '''Calculates Simple Interest.'''
    return principal * rate * years

def total_amount_simple_interest(principal: float, rate: float, years: float) -> float:
    '''Calculates total amount after simple interest.'''
    return principal + (principal * rate * years)