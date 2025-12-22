# Discount Factors Explained

Discount factors are fundamental in finance for determining the present value of future cash flows. They represent how much a future amount of money is worth today, given a specific interest rate and time period.
> **Important:**  
> The discount factor will **always** be less than 1. For example, if the discount factor is 0.96, it means your money is expected to lose 4% of its value over the specified period.

## Why Use Discount Factors?

When you expect to receive money in the future, that money is worth less than the same amount received today due to the time value of money. Discount factors help you convert future cash flows into their present value, allowing for fair comparisons and valuations.

## How Are Discount Factors Calculated?

A simple discount factor for a single period is calculated as:

```
Discount Factor = 1 / (1 + r * t)
```
- `r` is the interest rate for the period (expressed as a decimal, e.g., 0.03 for 3%)
- `t` is the time period (in years)

This formula assumes simple interest. For compounding interest, the formula would be:

```
Discount Factor = 1 / (1 + r) ** t
```

## Practical Use

Discount factors are used to:

- Price bonds and swaps
- Value future cash flows in investment analysis
- Construct yield curves

For example, if you expect to receive $100 in 2 years at a 5% interest rate, the present value is:

```
Present Value = $100 * Discount Factor
Discount Factor = 1 / (1 + 0.05 * 2) = 1 / 1.10 ≈ 0.909
Present Value = $100 * 0.909 = $90.90
```

## In Your Code

Your functions take lists of rates and tenors, calculate the discount factor for each period, and return a list of discount factors. These can then be used to value a series of future payments, such as those in a swap or bond.

Discount factors are essential for any financial calculation involving future