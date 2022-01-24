import pandas as pd
import io, pkgutil


def get_wards():
    data = pkgutil.get_data(__package__, '/components/wards.csv')
    df = pd.read_csv(io.BytesIO(data))
    return df.to_json(orient='index')
