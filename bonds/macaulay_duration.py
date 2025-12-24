import numpy as np

# Function to calculate Macaulay Duration
def macaulay_duration(face_value, coupon_rate, maturity, price, frequency=1):
    # Calculate coupon payment
    coupon_payment = face_value * coupon_rate / frequency
    # Yield to maturity approximation (required for discounting)
    # We'll use the bond price to estimate yield using numerical methods
    
    def bond_price(yield_rate):
        return sum([coupon_payment / (1 + yield_rate)**t for t in range(1, maturity + 1)]) + face_value / (1 + yield_rate)**maturity

    def price_diff(y):
        return bond_price(y) - price

    # Use Newton-Raphson method to estimate yield to maturity
    from scipy.optimize import newton
    ytm = newton(price_diff, x0=0.05)

    # Calculate Macaulay Duration
    duration = sum([(t * coupon_payment) / (1 + ytm)**t for t in range(1, maturity + 1)])
    duration += (maturity * face_value) / (1 + ytm)**maturity
    duration /= price

    return duration

# Inputs
face_value = 100
coupon_rate = 0.06
maturity = 5
price = 129.75
frequency = 2

# Calculate and print Macaulay Duration
duration = macaulay_duration(face_value, coupon_rate, maturity, price, frequency)
print(f"Macaulay Duration: {duration:.4f} years")
