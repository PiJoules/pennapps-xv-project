# Resizes all images stored in subfolders of /images folder

import cv2
import os
import os.path


def resize_imgs(training_dir, width, height, dest_dir=None):
    if dest_dir is None:
        dest_dir = training_dir + "_resized"
    os.makedirs(dest_dir)

    for root, dirs, files in os.walk(training_dir):
        for filename in files:
            if filename.endswith(".jpg"):
                img = cv2.imread(os.path.join(root, filename))
                img = cv2.resize(img, (width, height))
                cv2.imwrite(os.path.join(dest_dir, filename), img)


def get_args():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("training_dir",
                        help="Directory containing original training data.")
    parser.add_argument("--width", type=int, default=256, help="Target width.")
    parser.add_argument("--height", type=int, default=256,
                        help="Target height.")
    parser.add_argument("--dest-dir",
                        help="Destination directory to store resized images.")

    return parser.parse_args()


def main():
    args = get_args()
    resize_imgs(args.training_dir,
                args.width,
                args.height,
                dest_dir=args.dest_dir)

    return 0


if __name__ == "__main__":
    main()
