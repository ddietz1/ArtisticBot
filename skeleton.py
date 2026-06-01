import cv2
import numpy as np
import math

# Load the image and convert to grayscale
image = cv2.imread('popeye.jpg')
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
# contours, _ = cv2.findContours(skeleton, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

y_coords, x_coords = np.where(skeleton > 0)
unvisited_points = list(zip(x_coords, y_coords))

robot_paths = []
current_path = []

# --- TUNING PARAMETERS ---
target_spacing = 20.0  # Physical distance between dots (in pixels)
pen_up_distance = 30.0 # If the next dot is this far away, start a new path
# -------------------------

if unvisited_points:
    # Start the first path with the very first pixel we found
    current_point = unvisited_points.pop(0)
    current_path.append(current_point)

    while unvisited_points:
        # Convert to numpy arrays for fast distance math
        pts_array = np.array(unvisited_points)
        curr_array = np.array(current_point)
        
        # Calculate straight-line distance from our current point to ALL remaining points
        distances = np.linalg.norm(pts_array - curr_array, axis=1)
        
        # Find the index of the closest point
        closest_idx = np.argmin(distances)
        closest_dist = distances[closest_idx]
        closest_point = unvisited_points[closest_idx]

        # Scenario A: The gap is huge. Lift the pen and start a new stroke.
        if closest_dist > pen_up_distance:
            robot_paths.append(current_path) # Save the finished stroke
            current_path = []                # Reset
            current_point = unvisited_points.pop(closest_idx)
            current_path.append(current_point)
            continue

        # Scenario B: The point is far enough away to drop a dot based on our spacing rule.
        if closest_dist >= target_spacing:
            current_path.append(closest_point)
            current_point = unvisited_points.pop(closest_idx) # Move our current location
        
        # Scenario C: The point is too close. 
        else:
            # We don't drop a dot, but we remove it from the unvisited list 
            # so we don't get stuck in an infinite loop checking it.
            # Notice we do NOT update `current_point`, so we keep measuring 
            # from our last successfully placed dot!
            unvisited_points.pop(closest_idx)

    # Don't forget to save the very last path when the loop finishes
    if current_path:
        robot_paths.append(current_path)

# --- PREVIEW CODE ---
preview = np.zeros_like(image)
total_dots = 0

for dot_path in robot_paths:
    # Draw paths with alternating colors to easily see where the pen lifts
    color = tuple(np.random.randint(50, 255, 3).tolist()) 
    for point in dot_path:
        cv2.circle(preview, point, 2, color, -1)
        total_dots += 1
        
print(f"Total dots for robot to draw: {total_dots}")
cv2.imshow('Robot Paths (Nearest Neighbor)', preview)
cv2.waitKey(0)
cv2.destroyAllWindows()