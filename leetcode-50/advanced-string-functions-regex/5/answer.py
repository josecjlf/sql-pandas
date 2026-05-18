import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = (activities.groupby('sell_date')['product']
    .agg(
        num_sold=lambda x: x.nunique(),
        products=lambda x: ','.join(sorted(x.unique()))
    )
    .reset_index()
)

    return df