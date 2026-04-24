import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['pos1'] = logs['num'].shift(1)
    logs['pos2'] = logs['num'].shift(2)

    return logs[(logs['pos1'] == logs['pos2']) & (logs['pos1'] == logs['num'])][['num']].drop_duplicates().rename(columns={"num" : "ConsecutiveNums"})