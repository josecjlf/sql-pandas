import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
   
    queries['p_r'] = queries['rating'] < 3
    queries['quality_r'] = queries['rating'] / queries['position']

    df = queries.groupby("query_name").agg(
        quality=("quality_r", "mean"),
        total_queries=("query_name", "count"),
        poor_queries=("p_r", "sum")
    )

    df['poor_query_percentage'] = df['poor_queries'] / df['total_queries'] * 100

    df = df.reset_index()

    return df[['query_name', 'quality', 'poor_query_percentage']].round(2)