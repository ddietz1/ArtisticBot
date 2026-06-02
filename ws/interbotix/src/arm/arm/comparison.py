# Compare images to get SSIM and MSE scores

# imports
import os
import cv2
import numpy as np

from skimage.metrics import structural_similarity as ssim

def ssim_score(img1, img2):
    # Ensure identical dimensions
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # convert to grayscale
    if len(img1.shape) == 3:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # resize
    win = min(7, img1.shape[0], img1.shape[1])
    if win % 2 == 0:
        win -= 1
    # Compute the SSIM score
    ssim_score, diff_image = ssim(img1, img2, full=True, win_size=win)
    print(f"SSIM Similarity Score: {ssim_score:.4f}")
    return ssim_score

def calculate_mse(image_a, image_b):
    # Images must be the same size
    if image_a.shape != image_b.shape:
        image_b = cv2.resize(image_b, (image_a.shape[1], image_a.shape[0]))
        
    # Convert to float to avoid unsigned integer wrap-around errors
    diff = cv2.absdiff(image_a, image_b)
    error = np.mean(diff ** 2)
    return error

# load images
img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'smiley_face_dots.png')
robot_img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'robot_smiley.png')

image = cv2.imread(img_path)
robot_image = cv2.imread(robot_img_path)

# remove all pixels that are not brown for the robot image
hsv_robot = cv2.cvtColor(robot_image, cv2.COLOR_BGR2HSV)
lower_brown = np.array([0, 40, 40])
upper_brown = np.array([20, 255, 200])
robot_mask = cv2.inRange(hsv_robot, lower_brown, upper_brown)
robot_masked = cv2.bitwise_and(robot_image, robot_image, mask=robot_mask)
cv2.imshow('robot mask', robot_masked)

cv2.imshow('image', image)
cv2.imshow('robot', robot_image)
# _, thresh = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY_INV)
# _, thresh_robot = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY_INV)
_, thresh = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
_, robot_thresh = cv2.threshold(robot_masked, 127, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('binary image', thresh)
cv2.imshow('binary robot', robot_thresh)
cv2.waitKey(0)
# get scores

MSE_err = calculate_mse(thresh, robot_thresh)
print(f'MSE score is {MSE_err:.4f}')
SSIM_score = ssim_score(thresh, robot_thresh)
print(f'SSIM score is {SSIM_score:.4f}')