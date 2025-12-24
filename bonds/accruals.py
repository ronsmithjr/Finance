from datetime import date, timedelta

def coupon_period_days(start_date, end_date, frequency=2, day_count="30/360"):
    """
    Compute the denominator (days in coupon period) based on frequency and day count convention.
    
    Parameters:
    -----------
    start_date : datetime.date
        The start date of the coupon period.
    end_date : datetime.date
        The end date of the coupon period.
    frequency : int
        Number of coupon payments per year (e.g., 1=annual, 2=semiannual, 4=quarterly).
    day_count : str
        Day count convention. Options: "30/360", "Actual/Actual", "Actual/360".
    
    Returns:
    --------
    int or float
        Days in coupon period (denominator for accrued interest fraction).
    """
    
    if day_count == "30/360":
        # Each month = 30 days, year = 360 days
        return 360 // frequency
    
    elif day_count == "Actual/Actual":
        # Actual days between coupon dates
        return (end_date - start_date).days
    
    elif day_count == "Actual/360":
        # Actual days, but denominator scaled to 360
        return (end_date - start_date).days
    
    else:
        raise ValueError("Unsupported day count convention")

# Example usage:
if __name__ == "__main__":
    start = date(2025, 1, 1)
    end = date(2025, 7, 1)  # semiannual coupon
    print("30/360:", coupon_period_days(start, end, frequency=2, day_count="30/360"))
    print("Actual/Actual:", coupon_period_days(start, end, frequency=2, day_count="Actual/Actual"))
    print("Actual/360:", coupon_period_days(start, end, frequency=2, day_count="Actual/360"))

