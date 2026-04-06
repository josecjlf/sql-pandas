import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity[(activity['activity_date'] < '2019-07-28') & (activity['activity_date'] > '2019-06-27')]
    new = df.groupby('activity_date', as_index=False)['user_id'].nunique()
    new.rename(columns = {'activity_date' : 'day', 'user_id': 'active_users'}, inplace=True)
    return new