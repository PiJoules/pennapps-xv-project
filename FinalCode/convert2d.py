import cv2
import numpy as np
from matplotlib import pyplot as plt


def getBinaryEdges(filename):
    img = cv2.imread(filename, 0)

    assert img is not None, "Error imreading file '{}'".format(filename)

    edges = cv2.Canny(img, 100, 200)
    #edges_binary = edges.tolist()
    edges_binary = edges

    num_cols = len(edges_binary[0])
    for i in xrange(len(edges_binary)):
        for j in xrange(num_cols):
            #if edges_binary[i][j] > 0:
            #    edges_binary[i][j] = 1
            if edges[i, j] > 0:
                edges[i, j] = 1

    #return edges_binary
    return edges

