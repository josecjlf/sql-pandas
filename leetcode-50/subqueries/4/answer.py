import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    customer = customer.groupby("visited_on")['amount'].sum().reset_index()
    customer['7d'] = customer['amount'].rolling(window=7).sum()
    df = customer[customer['visited_on'] >= min(customer['visited_on']+pd.Timedelta(days=6))]
    df1 = df.groupby("visited_on")['7d'].sum().reset_index()
    df1['average_amount'] = (df1['7d'] / 7).round(2)
    df1 = df1.rename(columns={"7d":"amount"})
    return df1