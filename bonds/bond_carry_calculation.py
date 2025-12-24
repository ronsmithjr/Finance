from datetime import datetime

def calculate_bond_carry(notional, coupon_rate, accrual_days, day_count_basis=360):
    """
    Estimate carry for a fixed-rate bond position over a given accrual period.

    Parameters:
    - notional: float, face value of the bond
    - coupon_rate: float, annual coupon rate (e.g., 0.05 for 5%)
    - accrual_days: int, number of days to calculate carry over (e.g., 1 for daily P&L)
    - day_count_basis: int, day count convention (default 360)

    Returns:
    - carry_pnl: float, estimated carry P&L over the accrual period
    """
    annual_coupon = notional * coupon_rate
    daily_accrual = annual_coupon / day_count_basis
    carry_pnl = daily_accrual * accrual_days
    return carry_pnl

# Example usage
notional = 5_000_000       # $5 million face value
coupon_rate = 0.04         # 4% annual coupon
accrual_days = 1           # Daily carry

carry = calculate_bond_carry(notional, coupon_rate, accrual_days)
print(f"Estimated daily carry P&L: ${carry:,.2f}")
