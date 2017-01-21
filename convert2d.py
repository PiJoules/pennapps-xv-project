import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import feature


def getBinaryEdges(filename, sigma=0.33):
    img = cv2.imread(filename, 0)

    assert img is not None, "Error imreading file '{}'".format(filename)

    #v = np.median(img)
    #lower = int(max(0, (1.0 - sigma) * v))
    #upper = int(min(255, (1.0 + sigma) * v))
    #edges = cv2.Canny(img, lower, upper)
    #edges = feature.canny(img, sigma=6)
    edges = cv2.Canny(img, 100, 200)

    num_cols = len(edges[0])
    for i in xrange(len(edges)):
        for j in xrange(num_cols):
            if edges[i, j] > 0:
                edges[i, j] = 1

    return edges

