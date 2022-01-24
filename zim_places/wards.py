import pandas as pd


def get_wards():
    df = pd.read_csv("./zim_places/components/wards.csv")
    return df.to_json(orient='index')
