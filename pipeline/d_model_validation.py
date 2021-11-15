import joblib
import numpy as np

from sklearn.metrics import mean_absolute_error

from constant import DATA_TEST_CLEANED_PATH, XGB_MODEL_PATH
from helper import split_data, read_csv


NUMBER_TRIP_TEST = 20

DAYS_VAL = (-90, -60, -30, -20, -15, -10, -7, -6, -5, -3, -2, -1)


def pred_cumulative_demand_X(list_day_x, demand, X):
    somme = 0

    for v in range(len(list_day_x)-1, -1, -1):
        if list_day_x[v] >= X:
            somme += demand[v]        
        else:
            break
    return somme


def random_trip(data):
    trip_id = np.random.choice(data.trip_id.unique())
    return trip_id


def compute_pred_dem_cum(data, trip_id, model):
    remaining_demand_sale_x = {}
    res_trip_id = []
   
    trip_df = data.loc[(data['trip_id'] == trip_id)]

    for sal_day_x, remaining_demand in zip(trip_df.sale_day_x, trip_df.remaining_demand):
        remaining_demand_sale_x[sal_day_x] = remaining_demand

    X_test, y_test = split_data(trip_df)

    demand_prediction = model.predict(X_test)
    
    list_sale_day_x = list(X_test.sale_day_x)
    
    for d in DAYS_VAL:
        res_trip_id.append(int(pred_cumulative_demand_X(list_sale_day_x,demand_prediction,d)))
        
    return res_trip_id, remaining_demand_sale_x


def compare_Y(remaining_demand_sale_x):
    y_test = []
    for i in DAYS_VAL:
        if i in remaining_demand_sale_x:
            y_test.append(remaining_demand_sale_x[i])
        else:
            b = True
            while b:
                i += 1
                if i in remaining_demand_sale_x:
                    y_test.append(remaining_demand_sale_x[i])
                    b = False
                elif i == 0:
                    y_test.append(0)
                    b = False
    return y_test


def main():
    data_test_clean = read_csv(DATA_TEST_CLEANED_PATH)
    print(f"Test data loaded successfully from {DATA_TEST_CLEANED_PATH}.")
    xgb_model_bayes_optim = joblib.load(XGB_MODEL_PATH)
    print(f"Model loaded successfully from {XGB_MODEL_PATH}.")

    for _ in range(NUMBER_TRIP_TEST):
        trip_id = random_trip(data_test_clean)
        remaining_demand_sale_x_from_prediction, remaining_demand_sale_x_true = compute_pred_dem_cum(
            data_test_clean,
            trip_id,
            xgb_model_bayes_optim)
        remaining_demand_sale_x_true = compare_Y(remaining_demand_sale_x_true)
        mae_xgb = mean_absolute_error(remaining_demand_sale_x_from_prediction, remaining_demand_sale_x_true)
        print("remaining_demand_sale_x_from_prediction", remaining_demand_sale_x_from_prediction)
        print('remaining_demand_sale_x_true', remaining_demand_sale_x_true)
        print("MAE: ", mae_xgb)
        print('\n')
