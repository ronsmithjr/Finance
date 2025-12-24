
from datetime import datetime, timedelta
import pandas as pd
import sys



def generate_treasury_cash_flows(face_value=1000, coupon_rate=0.04, years=10, payments_per_year=2, settlement_date="2025-10-15", current_interest_rate = 0.04):
    """
    Calculate cash flows for a Treasury bond and return as a DataFrame.
    
    Parameters:
        face_value (float): Principal amount of the bond.
        coupon_rate (float): Annual interest rate (e.g., 0.04 for 4%).
        years (int): Bond maturity in years.
        payments_per_year (int): Number of coupon payments per year.
        settlement_date (str): Start date in YYYY-MM-DD format.
    
    Returns:
        pd.DataFrame: Table of cash flows with columns [Period, Payment Date, Cash Flow]
        settlement_date (date): Issue date
        maturity_date (date): Last payment date
    """
    cash_flows = []
    coupon_payment = face_value * coupon_rate / payments_per_year
    total_payments = years * payments_per_year
    start_date = datetime.strptime(settlement_date, "%Y-%m-%d")

    for i in range(1, total_payments + 1):
        payment_date = start_date + timedelta(days=365.25 / payments_per_year * i)
        cash_flow = coupon_payment
        if i == total_payments:
            cash_flow += face_value  # Add principal at maturity
        year_val = payment_date.year if i % payments_per_year == 0 else ""
        
        discount_factor = get_discount_factor(current_interest_rate, payments_per_year,i)
        cash_flows.append({
            "Year": year_val,
            "Period": i,
            "Payment Date": payment_date.date(),
            "Cash Flow": round(cash_flow, 2),
            "Discount Factor": discount_factor,
            "PV": round(cash_flow/discount_factor,2)
             
        })

    # Aggregate total cash flow and append as summary row
    total_cash_flow = sum(item["Cash Flow"] for item in cash_flows)
    total_pv = sum(item["PV"] for item in cash_flows)
    summary_row = {
        "Year": "Total",
        "Period": "",
        "Payment Date": "",
        "Cash Flow": round(total_cash_flow, 2),
        "Discount Factor": "",
        "PV": round(total_pv,2)
    }
    cash_flows.append(summary_row)

    df = pd.DataFrame(cash_flows)
    # Ensure 'Year' is the first column
    cols = ["Year", "Period", "Payment Date", "Cash Flow", "Discount Factor", "PV"]
    df = df[cols]
    # Format 'Cash Flow' with commas
    df["Cash Flow"] = df["Cash Flow"].apply(lambda x: f"{x:,.2f}" if isinstance(x, (int, float)) else x)
    return df, start_date.date(), cash_flows[-2]["Payment Date"]  # Also return settlement and maturity dates

def get_discount_factor(curr_interest_rate, payments_per_year, period):
    step1 = curr_interest_rate / payments_per_year
    step2 = 1 + step1
    step3 = step2 ** period
    retVal = round(step3, 8)
    return retVal

def save_cashflows_to_csv(df, filename):
    df.to_csv(filename, index = False)

if __name__ == "__main__":
     # Allow interest rate to be passed as an argument
    if len(sys.argv) >= 8:
        try:
            coupon_rate = float(sys.argv[1])            
            current_interest_rate = sys.argv[2]
            face_value = float(sys.argv[3])
            years = int(sys.argv[4])
            payments_per_year = int(sys.argv[5])
            settlement_date = sys.argv[6]
            # Validate settlement_date format
            try:
                datetime.strptime(settlement_date, "%Y-%m-%d")
            except ValueError:
                print(f"Error: settlement_date '{settlement_date}' is not in YYYY-MM-DD format. Using default 2025-10-15.")
                settlement_date = "2025-10-15"
        except ValueError:
            print("Invalid command-line arguments for bond parameters (coupon_rate, face_value, years, payments_per_year, or settlement_date). Using default values.")
            coupon_rate = 0.04
            current_interest_rate = 0.04
            face_value = 1000
            years = 10
            payments_per_year = 2
            settlement_date = "2025-10-15"
    else:
        coupon_rate = 0.04
        current_interest_rate = 0.04
        face_value=1000

        years=10
        payments_per_year=2
        settlement_date="2025-10-15"        
       

    df, settlement_date, maturity_date = generate_treasury_cash_flows(
        face_value=face_value,
        coupon_rate=coupon_rate,
        years=years,
        payments_per_year=payments_per_year,
        settlement_date=settlement_date
    )
    print(df)
    print(f"Settlement Date: {settlement_date}")
    print(f"Maturity Date: {maturity_date}")
    now_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = fr"S:\Finance\assets\bond_cash_flows_{now_str}.csv"
    save_cashflows_to_csv(df, filename)