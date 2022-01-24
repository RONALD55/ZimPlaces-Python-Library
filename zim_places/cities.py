import pandas as pd


def get_cities():
    df = pd.read_csv("./zim_places/components/cities.csv")
    return df.to_json(orient='index')
