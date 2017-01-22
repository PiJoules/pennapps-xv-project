from __future__ import print_function

import json

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
    parser.add_argument("--training-dir", default="training2",
                        help="Directory containing training data.")

    return parser.parse_args()


def main():
    args = get_args()

    #filename = "training2/image60.bag.jpg"
    #directory_path = "training2"
    if args.test_file:
        filename = args.test_file
    else:
        # Call gui program
        create_img(args.new_test)
        filename = args.new_test

    directory_path = args.training_dir

    if __debug__:
        print("Loading training data...")

    training = convert_original_2D(directory_path)  # dict[str, arr]

    if __debug__:
        print("Loaded {} samples of training data...:".format(len(training)))

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

