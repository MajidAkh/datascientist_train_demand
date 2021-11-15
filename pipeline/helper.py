import pandas as pd


def read_csv(filepath):
    df = pd.read_csv(filepath)
    return df


def split_data(df):
    X = df.drop(columns=['demand', 'trip_id'])
    y = df['demand']

    return X, y
