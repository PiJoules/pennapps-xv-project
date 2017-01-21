import cv2
import numpy as np

COLOR = (255, 255, 255)
RADIUS = 3

drawing = False
end_coords = (-1, -1)


def smoothen_drawing(img, coords1, coords2):
	dx = coords2[0] - coords1[0]
	dy = coords2[1] - coords1[1]
	distance = max(abs(dx), abs(dy))
	for i in range(distance):
		x = int(coords1[0] + float(i)/distance * dx)
		y = int(coords1[1] + float(i)/distance * dy)
		cv2.circle(img, (x, y), RADIUS, COLOR, -1)


def draw_circle(event, x, y, flags, param):
    global drawing, end_coords

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        end_coords = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img, (x, y), RADIUS, COLOR, -1)
            smoothen_drawing(img, end_coords, (x, y))
            end_coords = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (x, y), RADIUS, COLOR, -1)
        drawing = False

img = np.zeros((512, 512), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
