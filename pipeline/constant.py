import os


dirname = os.path.dirname(__file__)

MATERIAL_PATH = os.path.realpath(os.path.join(dirname, "../material"))
if not os.path.isdir(MATERIAL_PATH):
    raise NotADirectoryError(f"The material dir {MATERIAL_PATH} doesn't exist !")

TRAIN_PATH = os.path.join(MATERIAL_PATH, "train.lz4")
TEST_PATH = os.path.join(MATERIAL_PATH, "test.lz4")

DATA_PATH = os.path.realpath(os.path.join(dirname, "../data"))

DATATRAIN_PATH = os.path.join(DATA_PATH, "train.csv")
DATATEST_PATH = os.path.join(DATA_PATH, "test.csv")

DATA_TRAIN_CLEANED_PATH = os.path.join(DATA_PATH, "data_train_cleaned.csv")
DATA_TEST_CLEANED_PATH = os.path.join(DATA_PATH, "data_test_cleaned.csv")

MODEL_PATH = os.path.realpath(os.path.join(dirname, "../models"))
XGB_MODEL_PATH = os.path.join(MODEL_PATH, "XGBoost_demand.sav")
