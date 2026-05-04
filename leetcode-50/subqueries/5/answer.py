import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([
    request_accepted['requester_id'],
    request_accepted['accepter_id']], ignore_index=True)

    df = df.to_frame()
    df = df.rename(columns={0 : "id"})
    
    df = df.groupby("id").size().reset_index(name="num").sort_values(by="num", ascending=False).head(1)

    return df