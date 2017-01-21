from __future__ import print_function

import json

from convert2d import getBinaryEdges
from knn import knn
from original_2d_convertion import convert_original_2D

filename = "training2/image60.bag.jpg"
directory_path = "training2"

training=convert_original_2D(directory_path)  # dict[str, arr]
print("training data:", len(training))

# Convert mapping to lst
training_vec = [(k, v) for k, v in training.iteritems()]

test=getBinaryEdges(filename)  # 2d arr

results = knn(map(lambda x: x[1], training_vec), test, best_n=10)  # list[tuple[int, 2d arr]]

best_results = []
for i, img in results:
	best_results.append(training_vec[i])

print(map(lambda x: x[0], best_results))
