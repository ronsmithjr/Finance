from datetime import date

def calculate_swap_carry(notional, fixed_rate, float_rate, day_count_fixed, day_count_float, accrual_days):
    """
    (Receive Fixed, Pay Float)
    Estimate carry for a vanilla interest rate swap position.
    
    Parameters:
    - notional: float, notional amount of the swap
    - fixed_rate: float, annual fixed rate received (e.g., 0.025 for 2.5%)
    - float_rate: float, annual floating rate paid (e.g., 0.015 for 1.5%)
    - day_count_fixed: float, day count fraction for fixed leg (e.g., 0.5 for semiannual)
    - day_count_float: float, day count fraction for floating leg (e.g., 0.25 for quarterly)
    - accrual_days: int, number of days to calculate carry over (e.g., 1 for daily P&L)

    Returns:
    - carry_pnl: float, estimated carry P&L over the accrual period
    """
    # Annual carry from fixed and float legs
    fixed_leg_accrual = notional * fixed_rate * day_count_fixed
    float_leg_accrual = notional * float_rate * day_count_float

    # Net carry per full accrual period
    net_carry = fixed_leg_accrual - float_leg_accrual

    # Scale to desired accrual period
    carry_pnl = net_carry * (accrual_days / (day_count_fixed * 360))  # Assuming 360-day year

    return carry_pnl

# Example usage
notional = 10_000_000
fixed_rate = 0.03      # 3%
float_rate = 0.015     # 1.5%
day_count_fixed = 0.5  # Semiannual
day_count_float = 0.25 # Quarterly
accrual_days = 1       # Daily carry

carry = calculate_swap_carry(notional, fixed_rate, float_rate, day_count_fixed, day_count_float, accrual_days)
print(f"Estimated daily carry P&L: ${carry:,.2f}")
