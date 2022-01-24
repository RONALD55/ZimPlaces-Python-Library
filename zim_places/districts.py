import pandas as pd


def get_districts():
    df = pd.read_csv("./zim_places/components/districts.csv")
    return df.to_json(orient='index')

