import os

import lz4.frame

from constant import (DATA_PATH, DATATEST_PATH, DATATRAIN_PATH, TEST_PATH, TRAIN_PATH)

BUFFER_SIZE = 10000


def lz4_to_csv(input_file, output_file):
    with lz4.frame.open(input_file, mode='r') as fp:
        with open(output_file, mode='wb') as dest:
            bytes_written = fp.read(size=BUFFER_SIZE)
            while len(bytes_written) > 0:
                dest.write(bytes_written)
                bytes_written = fp.read(size=BUFFER_SIZE)


def main():
    if not os.path.isdir(DATA_PATH):
        os.mkdir(DATA_PATH)
    else:
        if os.path.isfile(DATATRAIN_PATH):
            os.unlink(DATATRAIN_PATH)
        if os.path.isfile(DATATEST_PATH):
            os.unlink(DATATEST_PATH)
    lz4_to_csv(TRAIN_PATH, DATATRAIN_PATH)
    lz4_to_csv(TEST_PATH, DATATEST_PATH)
