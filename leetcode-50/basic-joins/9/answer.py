import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    df = signups.merge(confirmations, on='user_id', how='left')
    df = df[['user_id', 'action']]
    df['t_f'] = (df['action'] == 'confirmed').astype(int)
    df1 = df.groupby("user_id").size().reset_index(name='contagem_total')
    df2 = df.groupby("user_id")['t_f'].sum().reset_index()
    df2['confirmation_rate']= df2['t_f']/df1['contagem_total']
    return df2[['user_id', 'confirmation_rate']].round(2)