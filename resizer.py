# Resizes all images stored in subfolders of /images folder

import cv2
import os
import os.path
import cPickle as pickle

from convert2d import getBinaryEdgesHelper


def pickle_imgs(training_dir, width, height):
    pickle_dir = training_dir + "_pickled"
    if not os.path.exists(pickle_dir):
        os.makedirs(pickle_dir)

    for root, dirs, files in os.walk(training_dir):
        for filename in files:
            if filename.endswith(".jpg"):
                pname = filename.split(".")[:-1]
                pname.append("p")
                pickle_path = os.path.join(pickle_dir, ".".join(pname))

                if os.path.exists(pickle_path):
                    continue

                img = cv2.imread(os.path.join(root, filename))
                img = cv2.resize(img, (width, height))
                with open(pickle_path, "wb") as f:
                    pickle.dump(getBinaryEdgesHelper(img), f)


def get_args():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("training_dir",
                        help="Directory containing original training data.")
    parser.add_argument("--width", type=int, default=256, help="Target width.")
    parser.add_argument("--height", type=int, default=256,
                        help="Target height.")

    return parser.parse_args()


def main():
    args = get_args()
    pickle_imgs(training_dir=args.training_dir,
                width=args.width,
                height=args.height)

    return 0


if __name__ == "__main__":
    main()
