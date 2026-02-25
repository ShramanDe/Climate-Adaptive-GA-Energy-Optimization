import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def basic_cleaning(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df
