import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = project.merge(employee, on='employee_id')
    df = df.groupby('project_id', as_index=False)['experience_years'].mean()
    df['experience_years'] = df['experience_years'].round(2)
    df = df.rename(columns={'experience_years':'average_years'})
    return df