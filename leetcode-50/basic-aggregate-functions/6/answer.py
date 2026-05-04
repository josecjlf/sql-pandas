import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions['trans_date'].dt.strftime('%Y-%m')
    transactions["ap_rp"] = (transactions["state"] == "approved").astype(int)
    transactions["ap_am"] = transactions["amount"] * (transactions["state"] == "approved")
    
    df = transactions.groupby(["month", "country"],dropna=False).agg(
        trans_count=("id","count"),
        approved_count=("ap_rp", "sum"),
        trans_total_amount=("amount", "sum"),
        approved_total_amount=("ap_am", "sum")
    ).reset_index()

    return df