
from datetime import datetime, timedelta
import pandas as pd
import sys
from macaulay_duration import calculate_macaulay_duration, prepare_duration_df
from weighted_average_life import calculate_weighted_average_life, calculate_wal,prepare_wal_df
from bond_analytics import bond_panel

def generate_meta_data(face_value=1000, 
                       coupon_rate=0.04, years=10, 
                       payments_per_year=2, settlement_date="2025-10-15", 
                       current_interest_rate = 0.04):
    meta_data = []
    # Calculate maturity date by adding years to settlement_date
    try:
       # settlement_dt = datetime.strptime(settlement_date, "%Y-%m-%d")

        if isinstance(settlement_date, datetime):
            settlement_dt = settlement_date
        elif isinstance(settlement_date, str):
            settlement_dt = datetime.strptime(settlement_date, "%Y-%m-%d")
        elif hasattr(settlement_date, 'strftime'):  # Handles datetime.date
            settlement_dt = datetime.strptime(settlement_date.strftime("%Y-%m-%d"), "%Y-%m-%d")
        else:
            raise ValueError("Invalid settlement_date type")



        maturity_dt = settlement_dt.replace(year=settlement_dt.year + years)
        maturity_date_str = maturity_dt.strftime("%Y-%m-%d")
    except (ValueError, TypeError) as e:
        print(f"Error calculating maturity date: {e}")
        print(f"settlement_date: {settlement_date}, years: {years}")
        maturity_date_str = "Error"
    meta_data.append({
        "Face Value": f"{face_value:,.2f}",
        "Coupon Rate": coupon_rate,
        "Settlement Date": settlement_date,
        "Periods Per Year": payments_per_year,
        "Maturity Date": maturity_date_str,
        "Current Interest Rate": current_interest_rate
    })
    meta_df = pd.DataFrame(meta_data)
   
   
    meta_df_pivoted = meta_df.T.reset_index()
    meta_df_pivoted.columns = ['Field', 'Value']
    return meta_df_pivoted


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
    df["PV"] = df["PV"].apply(lambda x: f"{x:,.2f}" if isinstance(x, (int, float)) else x)

    cash_flow_values = [item["Cash Flow"] for item in cash_flows if "Cash Flow" in item]

    return df, cash_flow_values, total_pv, cash_flows  # Also return settlement and maturity dates

def get_discount_factor(current_interest_rate, payments_per_year, period):
    periodic_rate = current_interest_rate / payments_per_year   #Step 1
    growth_factor = 1 + periodic_rate                           #Step 2
    compounded_factor = growth_factor ** period                 #Step 3
    discount_factor = round(compounded_factor, 8)               #Step 4
    return discount_factor

def save_cashflows_to_csv(df, filename):
    df.to_csv(filename, index = False)

def save_cashflows_to_csv(meta_df, df, filename):
    with open(filename, 'w', newline='') as f:
        meta_df.to_csv(f, index=False, header=False)
        f.write('\n')
        df.to_csv(f, index=False)

def save_cashflows_to_csv(meta_df, shock_data, df, filename):
    with open(filename, 'w', newline='') as f:
        meta_df.to_csv(f, index=False, header=False)
        f.write('\n')
        shock_data.to_csv(f, index = False)
        f.write('\n')
        df.to_csv(f, index=False)


if __name__ == "__main__":
    now_str = datetime.now().strftime("%Y%m%d_%H%M%S")   
     # Allow interest rate to be passed as an argument
    if len(sys.argv) >= 9:
        try:
            

            coupon_rate = float(sys.argv[1])            
            current_interest_rate = float(sys.argv[2])
            face_value = float(sys.argv[3])
            years = int(sys.argv[4])
            payments_per_year = int(sys.argv[5])
            settlement_date = sys.argv[6]
            file_name = sys.argv[7]
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
            file_name = fr"bond_cash_flows_{now_str}.csv" 
    else:
        coupon_rate = 0.04
        current_interest_rate = 0.04
        face_value=1000

        years=10
        payments_per_year=2
        settlement_date="2025-10-15"  
        
        file_name = fr"S:\Finance\assets\bond_cash_flows_{now_str}.csv"  
       

    df, cash_flow_values, total_pv, cash_flows = generate_treasury_cash_flows(
        face_value=face_value,
        coupon_rate=coupon_rate,
        years=years,
        payments_per_year=payments_per_year,
        settlement_date=settlement_date,
        current_interest_rate = current_interest_rate
    )

    meta_df = generate_meta_data(face_value, coupon_rate, years, payments_per_year,
                                 settlement_date, current_interest_rate)

    macaulay_duration = calculate_macaulay_duration(cash_flow_values[:-1], current_interest_rate, payments_per_year, total_pv)
    

    meta_data, shockdata = bond_panel(coupon_rate,years,current_interest_rate,payments_per_year,face_value)


    save_cashflows_to_csv(meta_data, shockdata, df, file_name)