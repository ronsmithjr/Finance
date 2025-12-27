import numpy as np
from datetime import datetime, timedelta

def accrued_interest(coupon, freq, last_coupon_date, settlement_date, face=100):
    """
    Computes accrued interest using Actual/Actual.
    """
    coupon_payment = coupon * face / freq

    # Actual days between last coupon and settlement
    accrued_days = (settlement_date - last_coupon_date).days

    # Actual days in coupon period
    next_coupon_date = last_coupon_date + timedelta(days=int(365/freq))
    period_days = (next_coupon_date - last_coupon_date).days

    return coupon_payment * accrued_days / period_days


def bond_panel_with_accrual(coupon, maturity, ytm, freq=2, face=100,
                            last_coupon_date=None, settlement_date=None):
    """
    Bloomberg-style analytics panel including:
    Price, Clean Price, Dirty Price, Accrued Interest,
    Duration, Modified Duration, Convexity,
    and price changes for ±25/50/100 bps.
    """

    # Default dates if not provided
    if last_coupon_date is None:
        last_coupon_date = datetime.today() - timedelta(days=90)
    if settlement_date is None:
        settlement_date = datetime.today()

    # --- Cash flow schedule ---
    periods = int(maturity * freq)
    dt = 1 / freq
    times = np.array([dt * (i + 1) for i in range(periods)])
    cashflows = np.full(periods, coupon * face / freq)
    cashflows[-1] += face

    # --- Discount factors ---
    df = 1 / (1 + ytm / freq) ** (np.arange(1, periods + 1))

    # --- Full (dirty) price ---
    dirty_price = np.sum(cashflows * df)

    # --- Accrued interest ---
    ai = accrued_interest(coupon, freq, last_coupon_date, settlement_date, face)

    # --- Clean price ---
    clean_price = dirty_price - ai

    # --- Macaulay Duration ---
    pv_times = times * cashflows * df
    macaulay = np.sum(pv_times) / dirty_price

    # --- Modified Duration ---
    modified = macaulay / (1 + ytm / freq)

    # --- Convexity ---
    convexity = np.sum(cashflows * df * times * (times + dt)) / (dirty_price * (1 + ytm / freq)**2)

    # --- Repricing for shocks ---
    shocks = np.array([-0.01, -0.005, -0.0025, 0.0025, 0.005, 0.01])
    shock_labels = ["-100 bp", "-50 bp", "-25 bp", "+25 bp", "+50 bp", "+100 bp"]
    prices_shocked = []

    for s in shocks:
        y_new = ytm + s
        df_new = 1 / (1 + y_new / freq) ** (np.arange(1, periods + 1))
        prices_shocked.append(np.sum(cashflows * df_new))

    # --- Print panel ---
    print("\n" + "="*65)
    print("                 BLOOMBERG-STYLE BOND ANALYTICS")
    print("="*65)
    print(f"Clean Price         : {clean_price:12.4f}")
    print(f"Accrued Interest    : {ai:12.4f}")
    print(f"Dirty Price (Full)  : {dirty_price:12.4f}")
    print(f"YTM                 : {ytm*100:12.3f}%")
    print(f"Macaulay Duration   : {macaulay:12.4f} years")
    print(f"Modified Duration   : {modified:12.4f}")
    print(f"Convexity           : {convexity:12.4f}")
    print("-"*65)
    print("  Shock       Repriced Price")
    print("-"*65)
    for lbl, p in zip(shock_labels, prices_shocked):
        print(f"{lbl:>7}     : {p:12.4f}")
    print("="*65 + "\n")


bond_panel_with_accrual(
    coupon=0.04,
    maturity=6,
    ytm=0.05,
    freq=2,
    last_coupon_date=datetime(2024, 10, 15),
    settlement_date=datetime(2025, 1, 15)
)
