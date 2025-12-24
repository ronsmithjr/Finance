from datetime import date

def accrued_interest(last_coupon, next_coupon, settlement, coupon_rate, face_value=1000,
                     frequency=2, day_count="30/360"):
    """
    Compute accrued interest in currency terms for a bond trade.
    
    Logic:
    - Numerator: days from (last_coupon + 1) up to (settlement - 1).
      Settlement date excluded.
    - Denominator: days from (last_coupon + 1) up to and including next_coupon.
      Start excluded, payment date included.
    - Accrued Interest = Coupon Payment × (Numerator / Denominator).
    
    Parameters
    ----------
    last_coupon : datetime.date
        Date of the last coupon payment.
    next_coupon : datetime.date
        Date of the next coupon payment.
    settlement : datetime.date
        Settlement date of the bond trade.
    coupon_rate : float
        Annual coupon rate (e.g., 0.06 for 6%).
    face_value : float, optional
        Bond face value (default = 1000).
    frequency : int, optional
        Number of coupon payments per year (default = 2 for semiannual).
    day_count : str, optional
        Day count convention. Options: "30/360", "Actual/Actual", "Actual/360".
    
    Returns
    -------
    float
        Accrued interest in currency terms.
    """

    # --- Denominator (days in coupon period) ---
    if day_count == "30/360":
        denominator = 360 // frequency
    else:
        denominator = (next_coupon - last_coupon).days  # exclude start, include end

    # --- Numerator (days since last coupon up to settlement) ---
    numerator = (settlement - last_coupon).days - 1  # exclude settlement

    # --- Coupon Payment ---
    coupon_payment = (coupon_rate * face_value) / frequency

    # --- Accrued Interest ---
    accrued_interest_value = coupon_payment * (numerator / denominator)

    return accrued_interest_value

if __name__ == "__main__":
    # Example usage:
    last_coupon = date(2025, 1, 1)
    next_coupon = date(2025, 7, 1)
    settlement = date(2025, 3, 15)

    ai = accrued_interest(last_coupon, next_coupon, settlement,
                        coupon_rate=0.06, face_value=1000,
                        frequency=2, day_count="Actual/Actual")

    print("Accrued Interest:", round(ai, 2))
