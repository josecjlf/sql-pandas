import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = visits[~visits['visit_id'].isin(transactions['visit_id'])]
    df = df[['customer_id']]
    #gp = df.groupby('customer_id', as_index=False).size()
    #gp = gp.rename(columns={'size': 'count_no_trans'})
    gp = df.groupby('customer_id', as_index=False).agg(count_no_trans=('customer_id', 'count'))
    return gp