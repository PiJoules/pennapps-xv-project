import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import feature
from cropimage import trimmed_image, pad_and_resize


def color_circle(img, x, y, r=2):
    h, w = img.shape
    img[max(0, y-r): min(h, y+r), max(0, x-r): min(w, x+r)] = 1


def getBinaryEdgesHelper(img, r=2):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Trim and resize
    # Assuming white background
    trimmed = trimmed_image(img)
    img = pad_and_resize(trimmed, 256, 256)

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

    # Expand edges
    new_edges = np.zeros((len(edges), num_cols))
    for y in xrange(len(edges)):
        for x in xrange(num_cols):
            if edges[y, x] > 0:
                # Color areas around
                color_circle(edges, x, y, r=r)

    return edges

def getBinaryEdges(filename, sigma=0.33, r=2):
    img = cv2.imread(filename)
    assert img is not None, "Error imreading file '{}'".format(filename)
    return getBinaryEdgesHelper(img, r=r)

