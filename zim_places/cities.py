import pandas as pd
import io, pkgutil


def get_cities():
    data = pkgutil.get_data(__package__, '/components/cities.csv')
    df = pd.read_csv(io.BytesIO(data))
    return df.to_json(orient='index')
