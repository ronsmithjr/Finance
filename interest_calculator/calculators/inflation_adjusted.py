def calculate_inflation_adjusted_rate(nominal: float, inflation:float):
    if not (0 <= nominal <= 1):
        raise ValueError("Nominal cannot be 0")
    step_1 = (1 + nominal) / (1 + inflation)
    step_2 = step_1 - 1
    return step_2