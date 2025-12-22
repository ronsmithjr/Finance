'''
Computes net cash flows per period.
'''

def net_cashflow(accrual: float, fixed_rate: float, floating_rate: float, receive_fixed=True) -> float:
    if receive_fixed:
        return accrual * (fixed_rate - floating_rate)
    else:
        return accrual * (floating_rate - fixed_rate)