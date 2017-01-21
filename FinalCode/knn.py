#/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq
import cv2


def knn(training, test, best_n):
    """
    Args:
        training (list[list[list[int]]]): List of 2d arrays
        test (list[list[int]]): 2d array test
        best_n (Optional[int]): Best n matches

    Returns:
        list[(int, list[list[int]])]: List of tuples containing the 2d arrays (the training data) ordered
            by similarity and its index in the original training data list.
    """
    training_with_indexes = [(i, img) for i, img in enumerate(training)]
    return heapq.nlargest(best_n, training_with_indexes, lambda x: similarity(x[1], test))


def similarity(img1, img2):
    """
    Generates similarity score between 2 images as 2d arrays.

    Args:
        img1 (list[list[int]])
        img2 (list[list[int]])

    Returns:
        int
    """
    # Find larger image form area
    perim1 = sum(img1.shape)
    perim2 = sum(img2.shape)
    if perim1 > perim2:
        larger = img1.copy()
        smaller = img2.copy()
    else:
        larger = img2.copy()
        smaller = img1.copy()

    # Resize smaller into larger
    larger_resized = cv2.resize(larger, (smaller.shape[1], smaller.shape[0]))
    img1 = larger_resized
    img2 = smaller

    score = 0
    for y in xrange(len(img1)):
        row1 = img1[y]
        row2 = img2[y]
        for x in xrange(len(row1)):
            elem1 = row1[x]
            elem2 = row2[x]

            if elem1 == elem2:
                score += 1
    return score


def main():
    test_data = [
        [0, 0, 1],
        [1, 0, 0],
        [1, 1, 0],
    ]

    # Scores: 4, 3, 6
    # Order: 2, 3, 1
    training_data = [
        [
            [1, 0, 1],
            [0, 1, 0],
            [0, 1, 1],
        ],
        [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 1],
        ],
        [
            [0, 0, 0],
            [1, 1, 0],
            [1, 1, 1],
        ],
    ]

    results = knn(training_data, test_data, best_n=len(training_data))

    assert results[0][0] == 2
    assert results[1][0] == 0
    assert results[2][0] == 1

    return 0


if __name__ == "__main__":
    main()

