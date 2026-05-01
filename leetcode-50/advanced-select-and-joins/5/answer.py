import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    g = products.groupby('product_id')['change_date'].min().reset_index()
    p1 = g[g['change_date'] > '2019-08-16']
    p1['price'] = 10
    p1 = p1[['product_id','price']]

    f = products[products['change_date'] <= '2019-08-16']

    p2 = f.sort_values(['product_id', 'change_date']).drop_duplicates('product_id', keep='last')
    p2 = p2[['product_id', 'new_price']]
    p2 = p2.rename(columns={'new_price': 'price'})
    result = pd.concat([p1, p2])
    

    return result