import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

COLOR = (0, 0, 0)
RADIUS = 3
THICKNESS = -1  # filled circle

img = None
drawing = False
end_coords = (-1, -1)


def smoothen_drawing(img, coords1, coords2):
    dx = coords2[0] - coords1[0]
    dy = coords2[1] - coords1[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(coords1[0] + float(i) / distance * dx)
        y = int(coords1[1] + float(i) / distance * dy)
        cv2.circle(img, (x, y), RADIUS, COLOR, THICKNESS)


def draw_circle(event, x, y, flags, param):
    global img, drawing, end_coords

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        end_coords = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img, (x, y), RADIUS, COLOR, THICKNESS)
            smoothen_drawing(img, end_coords, (x, y))
            end_coords = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (x, y), RADIUS, COLOR, THICKNESS)
        drawing = False


def create_img(filename="sketch.png", w=256, h=256):
    """
    Opens the window and saves the file.

    Returns:
        str: The file this image was saved in.
    """
    global img
    img = np.full((h, w), 255)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)

    while True:
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == 13:
            new_img = Image.fromarray(img)
            if new_img.mode != 'RGB':
                new_img = new_img.convert('RGB')
            new_img.save(filename)
            break

    cv2.destroyAllWindows()


def display_results(results):
    """
    Displays the original image and the best three matches.
    """
    title_dict = {
        1: "Original",
        2: "Best Match",
        3: "2nd Best Match",
        4: "3rd Best Match"
    }

    for i in xrange(4):
        plt.subplot(2, 2, i + 1),
        plt.imshow(cv2.imread(results[i]), cmap='gray')
        plt.title(title_dict[i + 1]), plt.xticks([]), plt.yticks([])

    plt.show()


def main():
    create_img()


if __name__ == "__main__":
    main()
