import datetime

import pandas as pd
import numpy as np

from constant import *
from helper import read_csv


def oneHotCatVars(df, df_cols):
    
    df_1 = df.drop(columns=df_cols, axis=1)
    df_2 = pd.get_dummies(df[df_cols])
    
    return pd.concat([df_1, df_2], axis=1, join='inner')


def preprocess(df_):
    
    df = df_.copy()
    #missing value
    df = df.drop(df[df.od_number_of_similar_2_hours < 0].index)
    
    trip_or_dest = [f"{start}{end}"
         for start, end in zip(df.origin_station_name, df.destination_station_name)]
    df['trip_or_dest'] = trip_or_dest
    #df = df.assign(trip_or_dest = lambda data: trip_or_dest)
    
    trip_id = [
        f"{datetime}{time}{start}{end}"
        for datetime, time, start, end in zip(df.departure_date,
                                              df.od_origin_time,
                                              df.origin_station_name,
                                              df.destination_station_name)]
    df['trip_id'] = trip_id

    sale_week = [
        datetime.date(year, month, day).isocalendar()[1]
        for year, month, day in zip(
            df.sale_year,
            df.sale_month,
            df.sale_day)
                ]
    df['sale_week'] = sale_week
    
    categorical_features_redondance = ['departure_date','sale_date','dataset_type','destination_station_name','origin_station_name']
    categorical_features_to_process = ['trip_or_dest']
    df = df.drop(columns=categorical_features_redondance)
    df = oneHotCatVars(df, categorical_features_to_process)

    df = df.join(
        df.groupby('trip_id')['price'].aggregate(['mean', 'min', 'max']), on='trip_id')

    # shift column 'Name' to first position
    first_column = df.pop('trip_id')
  
    # insert column using insert(position,column_name,
    # first_column) function
    df.insert(0, 'trip_id', first_column)
    
    # shift column 'Name' to first position
    second_column = df.pop('price')
  
    # insert column using insert(position,column_name,
    # first_column) function
    df.insert(1, 'price', second_column)
    return df


def main():

    data_train = read_csv(DATATRAIN_PATH) 
    print(f"Data train loaded successfully with initial features from {DATATRAIN_PATH}.")
    data_test = read_csv(DATATEST_PATH)  
    print(f"Data test loaded successfully with initial features from {DATATEST_PATH}.")

    data_train_clean = preprocess(data_train)
    print("Data train successfully processed.")
    data_test_clean = preprocess(data_test)
    print("Data test successfully processed.")

    data_train_clean.to_csv(DATA_TRAIN_CLEANED_PATH, index=False)
    print(f"Train data successfully saved into {DATA_TRAIN_CLEANED_PATH}.")
    data_test_clean.to_csv(DATA_TEST_CLEANED_PATH, index=False)
    print(f"Test data successfully saved into {DATA_TEST_CLEANED_PATH}.")
