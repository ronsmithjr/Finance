# Fixed Rate Calculation and Swap Valuation

## Fixed Rate Calculation

The function `calculate_fixed_rate(discount_factors: list) -> float` computes the fixed rate for a plain vanilla interest rate swap. The fixed rate is the rate that makes the present value of the fixed leg payments equal to the present value of the floating leg payments (assuming the floating leg is valued at par).

**How it works:**
- **Numerator:** `1 - discount_factors[-1]`  
  This represents the difference between the notional amount (1) and the present value of the notional repaid at the end of the swap (discounted by the last discount factor).
- **Denominator:** `sum(discount_factors)`  
  This is the sum of the present values of all fixed leg payments over the life of the swap.
- **Result:** The fixed rate is the ratio of these two values, giving the rate that equates the present value of fixed payments to the notional minus the present value of the final notional repayment.

This formula is standard in swap pricing and ensures the swap is fair at inception (i.e., its value is zero).

## Swap Valuation

The function `value_swap(fixed_leg: float, floating_leg: float) -> float` calculates the value of the swap by subtracting the present value of the floating leg from the present value of the fixed leg.

**How it works:**
- **Fixed Leg:** Present value of all fixed payments (using the fixed rate and discount factors).
- **Floating Leg:** Present value of all floating payments (often valued at par at reset).
- **Result:** If the value is positive, the fixed-rate receiver benefits; if negative, the floating-rate receiver benefits.

This approach allows you to determine whether the swap is in-the-money or out-of-the-money for either party, based on current market rates and discount factors.

---

**Summary:**  
- The fixed rate calculation ensures the swap is fair at inception.
- The swap valuation tells you the net value of the swap position, helping assess profit or