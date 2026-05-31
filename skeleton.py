import cv2
import numpy as np

# 1. Load the image and convert to grayscale
# image = cv2.imread('popeye.jpg')
image = cv2.imread('popeye.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2. Thresholding
# Anything darker than 127 becomes White (255), everything else becomes Black (0)
# We use THRESH_BINARY_INV because OpenCV tools prefer the subject to be white
_, binary = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

# 3. Skeletonization (Crush lines to 1 pixel wide)
skeleton = cv2.ximgproc.thinning(binary)

# 4. Find Contours (Create the robot paths)
contours, _ = cv2.findContours(skeleton, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# 5. Simplify the paths (Reduce the dots)
robot_paths = []
for contour in contours:
    # A 2-pixel epsilon usually preserves curves perfectly while dropping useless data
    approx = cv2.approxPolyDP(contour, 2, closed=False)
    
    # Filter out tiny specks (noise) so the robot doesn't draw random dots
    if len(approx) > 10: 
        robot_paths.append(approx)

# Create a blank black canvas to preview the robot's paths
preview = np.zeros_like(image)
cv2.drawContours(preview, robot_paths, -1, (0, 255, 0), 1)

cv2.imshow('1. Original Binary', binary)
cv2.imshow('2. Skeleton (1-pixel wide)', skeleton)
cv2.imshow('3. Final Robot Paths', preview)
cv2.waitKey(0)