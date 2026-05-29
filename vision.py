# Try to identify a triangle and decompose it into a list of x,y coordinates

import cv2
import numpy as np

image = cv2.imread("triangle.png")

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img_gray, 30, 200)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
approx = cv2.approxPolyDP(contours[0], 0.01, closed=True)
print(f'contour len:{len(contours[0])}, approx len:{len(approx)}')

cv2.imshow('Canny Edges after contouring', edges)

cv2.drawContours(image, contours, -1, (255, 0, 0), 3)
cv2.imshow('Contours', image)

cv2.drawContours(image, approx, -1, (0, 0, 255), 3)
cv2.imshow('Contours(approx)', image)
cv2.waitKey(0)
cv2.destroyAllWindows()