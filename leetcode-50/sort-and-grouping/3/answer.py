import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    array = sales.groupby('product_id', as_index=False)['year'].transform('min')
    result = sales[sales['year'] == array]
    result = result[['product_id','year','quantity','price']]
    result = result.rename(columns={'year':'first_year'})
    return result