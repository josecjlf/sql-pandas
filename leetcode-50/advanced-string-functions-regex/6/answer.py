import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders[(orders['order_date'] >= '2020-02-01') & (orders['order_date'] <= '2020-02-29')]
    df = products.merge(orders, on='product_id')
    df = df.groupby('product_name')['unit'].sum().reset_index()
    return df[df['unit'] >= 100]