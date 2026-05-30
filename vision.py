# Try to identify a triangle and decompose it into a list of x,y coordinates

import cv2
import numpy as np
import pyrealsense2 as rs

# Set up the realsense camera
pipeline = rs.pipeline()
config = rs.config()

# Enable the RGB color stream
config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)

# Start the camera stream
pipeline.start(config)

try:
    while True:
        # Wait for the next available frame
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        if not color_frame:
            continue

        # Convert the RealSense frame to a numpy array so OpenCV can process it
        image = np.asanyarray(color_frame.get_data())

        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        t_lower = 30
        t_upper = 230
        aperture_size = 3
        L2Gradient = True

        edges = cv2.Canny(img_gray, t_lower, t_upper,
                          apertureSize=aperture_size, L2gradient=L2Gradient)

        contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)

            epsilon = 1
            approx = cv2.approxPolyDP(largest_contour, epsilon, closed=True)

            print(f'contour len:{len(largest_contour)}, approx len:{len(approx)}')
            print(f'Limited contours: {approx}')

            cv2.drawContours(image, [largest_contour], -1, (255, 0, 0), 3)
            cv2.drawContours(image, [approx], -1, (0, 0, 255), 3)

        cv2.imshow('Canny Edges', edges)
        cv2.imshow('Contours', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    pipeline.stop()
    cv2.destroyAllWindows()




