import pandas as pd


def get_provinces():
    df = pd.read_csv("./zim_places/components/provinces.csv")
    return df.to_json(orient='index')
