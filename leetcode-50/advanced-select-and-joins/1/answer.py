import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(employees, left_on='employee_id', right_on='reports_to', suffixes=('','_r'))

    df = df.groupby(['employee_id','name'], as_index=False).agg(
        reports_count = ('employee_id_r', 'count'),
        average_age = ('age_r', 'mean')
    )
    df['average_age'] = (df['average_age'] + 0.5).astype(int)

    return df.sort_values(by = 'employee_id')