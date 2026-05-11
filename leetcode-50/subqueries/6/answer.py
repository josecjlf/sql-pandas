import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    mask_tiv = insurance['tiv_2015'].duplicated(keep=False)
    mask_loc = ~insurance.duplicated(['lat', 'lon'], keep=False)

    total = insurance[mask_tiv & mask_loc]['tiv_2016'].sum()

    return pd.DataFrame({'tiv_2016': [round(total, 2)]})