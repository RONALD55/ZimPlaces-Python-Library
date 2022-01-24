import pandas as pd
import io, pkgutil


def get_districts():
    data = pkgutil.get_data(__package__, '/components/districts.csv')
    df = pd.read_csv(io.BytesIO(data))
    return df.to_json(orient='index')
