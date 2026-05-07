import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    df = queue.sort_values(by="turn")
    df['total'] = df['weight'].cumsum()
    df = df[df['total'] <= 1000]
    df = df.iloc[[-1]]
    return df[['person_name']]