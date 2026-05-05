import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(employee, left_on='managerId', right_on='id', suffixes=('_l','_r'))
    df = df.groupby(["id_r", "name_r"], dropna=False).size().reset_index(name="count")
    df = df[df["count"] >= 5]
    df = df.rename(columns={"name_r":"name"})
    return df[['name']]