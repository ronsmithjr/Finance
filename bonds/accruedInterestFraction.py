from datetime import date

def accrued_interest_fraction(last_coupon, next_coupon, settlement, frequency=2, day_count="30/360"):
    """
    Compute the accrued interest fraction for dirty price calculation.
    
    Logic:
    - Numerator: days from (last_coupon + 1) up to (settlement - 1).
      Settlement date is excluded.
    - Denominator: days from (last_coupon + 1) up to and including next_coupon.
      Start excluded, payment date included.
    
    Parameters
    ----------
    last_coupon : datetime.date
        Date of the last coupon payment.
    next_coupon : datetime.date
        Date of the next coupon payment.
    settlement : datetime.date
        Settlement date of the bond trade.
    frequency : int
        Number of coupon payments per year (e.g., 2 = semiannual).
    day_count : str
        Day count convention. Options: "30/360", "Actual/Actual", "Actual/360".
    
    Returns
    -------
    float
        Accrued interest fraction (numerator/denominator).
    """

    # --- Denominator (days in coupon period) ---
    if day_count == "30/360":
        denominator = 360 // frequency
    else:
        denominator = (next_coupon - last_coupon).days  # exclude start, include end

    # --- Numerator (days since last coupon up to settlement) ---
    numerator = (settlement - last_coupon).days - 1  # exclude settlement

    return numerator / denominator

if __name__ == "__main__":
    # Example usage:
    last_coupon = date(2025, 1, 1)
    next_coupon = date(2025, 7, 1)
    settlement = date(2025, 3, 15)

    fraction = accrued_interest_fraction(last_coupon, next_coupon, settlement, frequency=2, day_count="Actual/Actual")
    print("Accrued Interest Fraction:", fraction)
