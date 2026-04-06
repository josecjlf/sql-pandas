import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    counts = employee.groupby('employee_id')['department_id'].transform('count')
    df = employee[(employee['primary_flag'] == 'Y') | (counts == 1)]
    return df[['employee_id', 'department_id']]

