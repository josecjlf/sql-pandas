import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    df = weather.sort_values('recordDate')
    df['prev_temp'] = df['temperature'].shift(1)
    df['prev_date'] = df['recordDate'].shift(1)

    result = df[(df['recordDate'] == df['prev_date'] + pd.Timedelta(days=1)) & (df['temperature'] > df['prev_temp'])]

    return result[['id']]