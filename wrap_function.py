from __future__ import print_function

import json
import cv2

from convert2d import getBinaryEdges
from knn import knn
from original_2d_convertion import convert_original_2D

filename = "training2/image1.pikachu.jpg"
directory_path = "training2"

training=convert_original_2D(directory_path)  # dict[str, arr]
print("training data:", len(training))

# Convert mapping to lst
training_vec = [(k, v) for k, v in training.iteritems()]

img = cv2.imread(filename, 0)
assert img is not None, "Error imreading file '{}'".format(filename)
num_cols = len(img[0])
for i in xrange(len(img)):
    for j in xrange(num_cols):
        if img[i, j] > 0:
            img[i, j] = 1
test = img

results = knn(map(lambda x: x[1], training_vec), test, best_n=10)  # list[tuple[int, 2d arr]]

best_results = []
for i, img in results:
	best_results.append(training_vec[i])

print(map(lambda x: x[0], best_results))

