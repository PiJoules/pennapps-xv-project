import cv2
import numpy as np
from matplotlib import pyplot as plt



def getBinaryEdges(filename):
    img = cv2.imread(filename, 0)

    # img = cv2.GaussianBlur(img, (5, 5), 0)
    # edges = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
    edges = cv2.Canny(img, 100, 200)
    # edges = feature.canny(img, sigma=6)

    edges_binary = edges.tolist()

    num_cols = len(edges_binary[0])
    for i in xrange(len(edges_binary)):
        for j in xrange(num_cols):
            if edges_binary[i][j] > 0:
                edges_binary[i][j] = 1

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges_binary, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()

    return edges_binary


def main():
    getBinaryEdges("pikachu.jpg")


if __name__ == "__main__":
    main()
