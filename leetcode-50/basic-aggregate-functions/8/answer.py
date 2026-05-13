import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
      activity["first"] = activity.groupby("player_id")['event_date'].transform(min)
      activity_2nd_day = activity[activity["first"] + pd.Timedelta(days=1) == activity["event_date"]]
      df = pd.DataFrame({"fraction":[(len(activity_2nd_day) / activity['player_id'].nunique())]})
      return df.round(2)