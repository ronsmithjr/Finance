def calculate_daily_interest(principal, annual_rate, days_accrued, year_days=365, output_format='text'):
    interest = principal * (annual_rate / year_days) * days_accrued

    if output_format == 'json':
        import json
        return json.dumps({
            "principal":principal,
            "annual_rate": annual_rate,
            "days_accrued": days_accrued,
            "daily_intrest": round(interest,2)
        }, indent=2)
    elif output_format == 'dict':
        return{
           "principal":principal,
            "annual_rate": annual_rate,
            "days_accrued": days_accrued,
            "daily_intrest": round(interest,2)
        }
    else:
        return f"Daily interest over {days_accrued} days: ${round(interest,2)}"