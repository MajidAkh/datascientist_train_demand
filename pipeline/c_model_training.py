import os

import joblib
from xgboost import XGBRegressor

from constant import DATA_TRAIN_CLEANED_PATH, XGB_MODEL_PATH, MODEL_PATH
from helper import read_csv, split_data

REFRESH_MODEL = True


def fit_model(X_t, y_t, model, early_stop):
    model.fit(X_t, y_t, early_stopping_rounds=early_stop, eval_set=[(X_t, y_t)], verbose=False)
    
    joblib.dump(model, XGB_MODEL_PATH)

    return model


def main():
    data_train_clean = read_csv(DATA_TRAIN_CLEANED_PATH)
    print(f"Train data loaded successfully from {DATA_TRAIN_CLEANED_PATH}.")

    X_train, y_train = split_data(data_train_clean)
    print("Train data splited")
    if not os.path.isdir(MODEL_PATH):
        os.mkdir(MODEL_PATH)

    if not os.path.exists(XGB_MODEL_PATH):
        print("Launch training! Please wait.")
        xgb_model_bayes_optim = XGBRegressor(
                objective='reg:squarederror',
                colsample_bytree=0.67,
                gamma=5,
                learning_rate=0.01,
                max_depth=11,
                min_child_weight=7,
                n_estimators=500,
                reg_alpha=40,
                reg_lambda=0.58,
                subsample=0.75)
        fit_model(X_train, y_train, xgb_model_bayes_optim, 5)
        print(f'XGBoost demand model trained and saved to {XGB_MODEL_PATH}.')
    else:
        print(f"Found model {XGB_MODEL_PATH}! If you want to retrain the model, delete the existing one!")
