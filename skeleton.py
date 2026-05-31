import cv2
import numpy as np

# Load the image and convert to grayscale
image = cv2.imread('smiley_face.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Thresholding
# Anything darker than lower_threshold becomes White, everything else becomes 
# Black (0)
lower_threshold = 50
upper_threshold = 255
_, binary = cv2.threshold(gray, lower_threshold, upper_threshold, 
                          cv2.THRESH_BINARY_INV)

binary = cv2.copyMakeBorder(binary, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)

# Skeletonization (Crush lines to 1 pixel wide)
skeleton = cv2.ximgproc.thinning(binary)

# Find Contours (Create the robot paths)
contours, _ = cv2.findContours(skeleton, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# Simplify the paths (Reduce the dots)
dot_spacing = 1 # This is the min distance between points in the final path.
target_dot_count = 300
total_dots = float('inf')

# Loop through contours and keep only every nth point until there are a 
# resonable number of points for the robot to draw
while total_dots > target_dot_count:
    robot_paths = []
    for contour in contours:
        # Filter out tiny specks so the robot doesn't draw random dots
        if len(contour) > dot_spacing: 
            spaced_points = contour[::dot_spacing]  # Take every nth point
            robot_paths.append(spaced_points)

    total_dots = sum(len(path) for path in robot_paths)
    if total_dots > target_dot_count:
        dot_spacing += 1 
print(f"Dot spacing: {dot_spacing}, Total dots for robot to draw: {total_dots}")
# Create a blank black canvas to preview the robot's paths
preview = np.zeros_like(image)

for dot_path in robot_paths:
    for point in dot_path:
        x, y = point[0]
        # Draw green dots for the robot to follow
        cv2.circle(preview, (x, y), 3, (0, 255, 0), -1) 
        
print(f"Total dots for robot to draw: {sum(len(path) for path in robot_paths)}")
cv2.imshow('1. Original Binary', binary)
cv2.imshow('2. Skeleton (1-pixel wide)', skeleton)
cv2.imshow('3. Final Robot Paths', preview)
cv2.waitKey(0)