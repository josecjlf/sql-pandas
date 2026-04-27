import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    df = users.merge(register, on="user_id").groupby("contest_id").size().reset_index(name="percentage")
    total = len(users['user_id'])
    df['percentage'] = ((df['percentage'] / total) * 100).round(2)
    df = df.sort_values(by=['percentage','contest_id'], ascending=[False, True])
    return df