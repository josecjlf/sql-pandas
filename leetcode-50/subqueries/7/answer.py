import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department,left_on='departmentId',right_on='id')

    df = df[df.groupby('id_y')['salary'].rank(method='dense', ascending=False) <= 3]

    final = df[['name_y', 'name_x', 'salary']]

    final = final.rename(columns={'name_y': 'Department','name_x': 'Employee','salary': 'Salary'})

    return final