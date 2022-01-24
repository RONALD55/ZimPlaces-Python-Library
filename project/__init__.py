import pandas as pd


def cities():
    df = pd.read_csv("./project/components/cities.csv")
    return df.to_json(orient='index')


def provinces():
    df = pd.read_csv("./project/components/provinces.csv")
    return df.to_json(orient='index')


def wards():
    df = pd.read_csv("./project/components/wards.csv")
    return df.to_json(orient='index')


def districts():
    df = pd.read_csv("./project/components/districts.csv")
    return df.to_json(orient='index')

