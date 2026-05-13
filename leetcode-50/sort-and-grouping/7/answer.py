import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers.groupby("num").agg(
        p_num = ("num", "count")
    ).reset_index()
    result = df[df['p_num'] == 1].sort_values(by='num', ascending=False)[['num']].head(1)
    
    if result.empty:
        return pd.DataFrame({'num': [None]})

    return result