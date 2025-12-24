"""
Sequential Pay CMO Structure
Tranch A receives all available principal until it is fully paid down
Tranch B receives all principal until fully paid
Then C, etc.
"""

import pandas as pd

class Tranche:
    def __init__(self, name, initial_balance, coupon):
        self.name = name
        self.initial_balalnce = initial_balance
        self.coupon = coupon
        self.balance = initial_balance
        self.cash_flows = []

    def add_cashflow(self, month, interest, principal):
        self.cashflows.append({
            "month": month,
            "begin_balance": self.balance,
            "interest": interest,
            "principal": principal,
            "total_cash": interest + principal
        })
        self.balance -= principal
    
    def to_frame(self):
        df = pd.DataFrame(self.cash_flows)
        if not df.empty:
            df["end_balance"] = df["begin_balance"] - df["principal"]
        return df