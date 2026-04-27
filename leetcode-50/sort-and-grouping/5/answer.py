import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    df = queries.copy()

    df["quality_part"] = df["rating"].astype(float) / df["position"]
    df["poor_part"] = (df["rating"] < 3).astype(int)

    result = (
        df.groupby("query_name", as_index=False)
          .agg(
              quality=("quality_part", "mean"),
              poor_query_percentage=("poor_part", "mean")
          )
    )

    result["poor_query_percentage"] *= 100

    return result.round(2)