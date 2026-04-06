import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    sales = sales.merge(product, on='product_id')
    return sales[['product_name','year','price']]