def calculate_effective_rate(nominal_rate: float, number_of_periods:int):
    if not (0 <= nominal_rate <= 1):
        raise ValueError("The Nominal rate must be between 0 and 1")
    
    step_1 = nominal_rate / number_of_periods
    step_2 = 1 + step_1
    step_3 = step_2 ** number_of_periods
    step_4 = step_3 - 1
    return step_4