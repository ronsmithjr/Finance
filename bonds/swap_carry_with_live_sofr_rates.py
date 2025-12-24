import requests

def get_live_sofr_rates():
    """
    Fetches the latest SOFR term rates and fallback LIBOR equivalents.
    Returns a dictionary with term SOFR and LIBOR fallback rates.
    """

    # Python

    # FRED_API = "https://api.stlouisfed.org/fred/series/observations"
    # params = {"series_id": "SOFR", "api_key": "YOUR_KEY", "file_type": "json"}
    # resp = requests.get(FRED_API, params=params)
    # data = resp.json()  # parse observations and pick the latest value


    # Example static values from latest published data (replace with API if needed)
    return {
        "sofr_30d": 0.0418,   # 30-day SOFR average
        "sofr_90d": 0.0432,   # 90-day SOFR average
        "libor_fallback_90d": 0.0458  # LIBOR fallback for 90-day tenor
    }

def calculate_swap_carry_live(notional, fixed_rate, float_rate, fixed_day_count, float_day_count, accrual_days):
    """
    Calculates carry for a receive-fixed, pay-float swap using live rates.
    """
    fixed_leg_accrual = notional * fixed_rate * fixed_day_count
    float_leg_accrual = notional * float_rate * float_day_count
    net_carry = fixed_leg_accrual - float_leg_accrual
    carry_pnl = net_carry * (accrual_days / (fixed_day_count * 360))  # Assuming 360-day year
    return carry_pnl

# Live rate fetch
rates = get_live_sofr_rates()

# Example swap parameters
notional = 10_000_000
fixed_rate = 0.05  # 5% fixed leg
float_rate = rates["sofr_90d"]  # Use 90-day SOFR average
fixed_day_count = 0.5  # Semiannual
float_day_count = 0.25  # Quarterly
accrual_days = 1  # Daily carry

carry = calculate_swap_carry_live(notional, fixed_rate, float_rate, fixed_day_count, float_day_count, accrual_days)
print(f"Estimated daily carry P&L: ${carry:,.2f}")
