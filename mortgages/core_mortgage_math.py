'''
Core mortgage math (single loan)
'''

import numpy as np
import pandas as pd


def level_payment_mortgage(principal, annual_rate, term_months):
    i = annual_rate / 12
    M = principal * (i / 1 - (1 + i) ** (-term_months))
    return M