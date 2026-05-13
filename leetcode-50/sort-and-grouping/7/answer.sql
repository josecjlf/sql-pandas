import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = customer.sort_values(by="customer_id")
    df = df.drop_duplicates(['customer_id','product_key'], keep='last')
    total = product.shape[0]
    df = df.groupby('customer_id').size().reset_index(name="temp")
    df = df[df['temp'] == total]
    return df[['customer_id']]