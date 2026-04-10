import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:

    max_id= seat['id'].max()

    def classificar(id):
        if id % 2 != 0 and id == max_id:
            return id
        elif id % 2 != 0:
            return id+1
        else:
            return id-1

    seat['id'] = seat['id'].apply(classificar)
    return seat.sort_values('id', ascending=True)