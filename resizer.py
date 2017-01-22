# Resizes all images stored in subfolders of /images folder

from __future__ import print_function

import cv2
import os
import os.path
import cPickle as pickle
import errno

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


def safe_mkdir(dirname):
    try:
        os.makedirs(dirname)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise OSError(e)


def pickle_filename(img_basename):
    return img_basename + ".p"


def pickle_images(images_dir, w=256, h=256, dest_dir=None, lim=5):
    if dest_dir is None:
        dest_dir = "pickled_training_data"

    safe_mkdir(dest_dir)

    for root, dirs, files in os.walk(images_dir):
        count = 0
        for filename in files:
            if count < lim and filename.endswith(".jpg"):
                # Get parent dir
                immediate_parent_dir = os.path.basename(root)  # apple, bag, etc.
                basename = filename[:-4] + "." + immediate_parent_dir  # image0.apple

                # Create pickle path
                p_file = os.path.join(dest_dir, pickle_filename(basename))  # pickled_training_data/image0.apple.p

                # Check if it exists first before creating pickle
                if not os.path.exists(p_file):
                    # Create the pickle
                    if __debug__:
                        print("pickling img", filename, "into", p_file)
                    img = cv2.imread(os.path.join(root, filename))
                    img = cv2.resize(img, (w, h))
                    with open(p_file, "wb") as f:
                        pickle.dump(getBinaryEdgesHelper(img), f)
                else:
                    if __debug__:
                        print("skipping pickle for", filename, "since it already exists as", p_file)
                count += 1


def get_args():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("training_dir",
                        help="Directory containing original training data.")
    parser.add_argument("--width", type=int, default=256, help="Target width.")
    parser.add_argument("--height", type=int, default=256,
                        help="Target height.")
    parser.add_argument("--target-dir", help="Destination dir to store the pickles.")
    parser.add_argument("--lim", type=int, default=5,
                        help="Max number of files in a sub dir to check.")

    return parser.parse_args()


def main():
    args = get_args()
    #pickle_imgs(training_dir=args.training_dir,
    #            width=args.width,
    #            height=args.height)
    pickle_images(args.training_dir,
                  w=args.width,
                  h=args.height,
                  dest_dir=args.target_dir,
                  lim=args.lim)

    return 0


if __name__ == "__main__":
    main()
