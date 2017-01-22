from __future__ import print_function

import json
import os
import cPickle as pickle

from convert2d import getBinaryEdges
from knn import knn
from original_2d_convertion import convert_original_2D
from gui import create_img


def get_args():
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument("--new-test", type=str, default="sketch.png",
                        help="New test file to create from gui.")
    parser.add_argument("--test-file", help="Image to classify.")
    parser.add_argument("--training-dir", default="pickled_training_data",
                        help="Directory containing training data.")

    return parser.parse_args()


def load_pickled_training_data(pickle_dir):
    data = {}
    for p_file in os.listdir(pickle_dir):
        full_path = os.path.join(pickle_dir, p_file)
        with open(full_path) as f:
            try:
                bin_arr = pickle.load(f)
            except Exception as e:
                raise RuntimeError("Unable to open pickle file {}".format(full_path))
            data[full_path] = bin_arr
    return data


def main():
    args = get_args()

    if args.test_file:
        filename = args.test_file
    else:
        # Call gui program
        create_img(args.new_test)
        filename = args.new_test

    directory_path = args.training_dir

    if __debug__:
        print("Loading training data...")

    #training = convert_original_2D(directory_path)  # dict[str, arr]
    training = load_pickled_training_data(directory_path)

    if __debug__:
        print("Loaded {} samples of training data...".format(len(training)))

    # Convert mapping to lst
    training_vec = [(k, v) for k, v in training.iteritems()]

    if __debug__:
        print("Performing edge detection on test data...")

    test = getBinaryEdges(filename)  # 2d arr

    if __debug__:
        print("Performing classification on input...")

    results = knn(map(lambda x: x[1], training_vec), test, best_n=10)  # list[tuple[int, 2d arr]]

    best_results = []
    for i, img in results:
        best_results.append(training_vec[i])

    print("best results:")
    print(map(lambda x: x[0], best_results))

    return 0


if __name__ == "__main__":
    main()

