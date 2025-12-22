def calculate_continuous_compounded(principal: float, annual_rate: float, time_in_years: int):
    EULER: float = 2.71828

    if not(0 <= annual_rate <= 1):
        raise ValueError("The Annual Rate must be between 0 and 1")
    
    step_1 = EULER ** (annual_rate * time_in_years)
    step_2 = principal * step_1
    return step_2