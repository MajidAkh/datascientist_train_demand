#!/usr/bin/env python3


import a_extract_data
import b_preprocessingdata
import c_model_training
import d_model_validation


def main():

    #Step 0: Extract data
    a_extract_data.main()
    print('Step 0: has been passed!')

    #Step 1: Preprocessing the data
    b_preprocessingdata.main()
    print('Step 1: has been passed!')

    #Step 2: Model training
    c_model_training.main()
    print('Step 2: has been passed!')

    #Step 3: Model validation
    d_model_validation.main()
    print('Step 3: has been passed!')


if __name__ == "__main__":
    main()
