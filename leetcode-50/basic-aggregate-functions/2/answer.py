import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = prices.merge(units_sold, on='product_id', how='left')
    df = df[(df['purchase_date'] <= df['end_date']) & (df['purchase_date'] >= df['start_date'])]
    df['total'] = df['units'] * df['price']
    result = df.groupby('product_id', as_index=False).agg({
        'total':'sum',
        'units':'sum'
    })
    result['average_price'] = (result['total'] / result['units']).round(2)

    result = prices[['product_id']].drop_duplicates().merge(
        result, on='product_id', how='left'
    )
    
    result['average_price'] = result['average_price'].fillna(0)
    
    return result[['product_id', 'average_price']]