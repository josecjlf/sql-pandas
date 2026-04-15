import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    def is_triangle(row):
        if (row['x']+row['z']>row['y'] and row['z']+row['y']>row['x'] and row['x']+row['y']>row['z']):
            return 'Yes'
        else:
            return 'No'

    triangle['triangle'] = triangle.apply(is_triangle, axis=1)
    return triangle