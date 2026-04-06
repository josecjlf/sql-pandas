import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[(views['author_id'] == views['viewer_id'])]
    df.rename(columns = {'author_id' : 'id'}, inplace=True)
    df = df.sort_values(by='id', ascending = True)
    df = df[['id']]
    df = df.drop_duplicates()
    return df