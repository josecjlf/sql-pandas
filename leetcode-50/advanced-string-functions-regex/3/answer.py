import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    df = employee.drop_duplicates('salary').sort_values(by='salary', ascending=False)

    if df.shape[0] < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    return pd.DataFrame({
        'SecondHighestSalary': [df.iloc[1]['salary']]
    })