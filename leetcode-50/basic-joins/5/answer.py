import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby(["machine_id", "process_id"]).agg(
        max = ("timestamp", "max"),
        min = ("timestamp", "min")
    ).reset_index()

    df['diff'] = df['max'] - df['min']

    result_df = df.groupby("machine_id")['diff'].mean().reset_index(name="processing_time")
    result_df['processing_time'] = result_df['processing_time'].round(3)
    

    return result_df