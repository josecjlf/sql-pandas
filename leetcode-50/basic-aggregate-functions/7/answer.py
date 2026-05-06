import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    df = delivery.sort_values(by=["customer_id", "order_date"])
    df = df.drop_duplicates('customer_id', keep='first')
    x1 = sum(df['order_date'] == df['customer_pref_delivery_date'])
    x2 = sum(df['order_date'] != df['customer_pref_delivery_date'])
    x3 = (x1/(x1+x2) * 100)
    x3 = round(x3, 2)

    final = pd.DataFrame({
    'immediate_percentage': [x3],})

    return final