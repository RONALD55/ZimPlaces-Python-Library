import pandas as pd
import io, pkgutil


def get_provinces():
    data = pkgutil.get_data(__package__, '/components/provinces.csv')
    df = pd.read_csv(io.BytesIO(data))
    return df.to_json(orient='index')
