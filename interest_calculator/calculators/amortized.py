def calculate_amortized_payment(principal: float, annual_rate: float, years: int ,periods_per_year: int = 12) -> float:
    r = (annual_rate / 100) / periods_per_year
    n = years * periods_per_year
    payment = principal * (r * (1 + r)**n) /((1 + r)**n - 1)
    return round(payment,2)

def generate_amortization_schedule(principal: float, annual_rate: float, years: int, periods_per_year: int = 12) -> list:
    r = (annual_rate / 100) / periods_per_year
    n = years * periods_per_year

    payment = calculate_amortized_payment(principal, annual_rate, years, periods_per_year)
    balance = principal
    schedule = []

    for period in range(1, n + 1):
        interest = round(balance * r, 2)
        principal_paid = round(payment - interest, 2)
        balance = round(balance - principal_paid, 2)
        schedule.append({
            "Period":period,
            "Payment": payment,
            "Principal Paid": principal_paid,
            "Interest Paid": interest, 
            "Remaining Balance":max(balance,0)
        })
    return schedule