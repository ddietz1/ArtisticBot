# Try to identify a triangle and decompose it into a list of x,y coordinates

import cv2
import numpy as np
import pyrealsense2 as rs
import argparse
import sys

def process_image(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    t_lower = 30
    t_upper = 230
    aperture_size = 3
    L2Gradient = True

    edges = cv2.Canny(img_gray, t_lower, t_upper,
                      apertureSize=aperture_size, L2gradient=L2Gradient)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    simplified_contours = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01, closed=False)
        simplified_contours.append(approx)

    if contours:
        cv2.drawContours(image, simplified_contours, -1, (255, 0, 0), 3)
    cv2.imshow('Canny Edges', edges)
    cv2.imshow('Contours', image)


def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Edge detection using RealSense camera or a static image.")
    parser.add_argument('--source', type=str, choices=['camera', 'image'], default='camera',
                        help="Choose input source: 'camera' (default) or 'image'")
    parser.add_argument('--filepath', type=str, default='test.jpg',
                        help="Path to the image file (only used if --source is 'image')")
    
    args = parser.parse_args()

    # Image Mode
    if args.source == 'image':
        print(f"Loading image from: {args.filepath}")
        image = cv2.imread(args.filepath)
        
        if image is None:
            print(f"Error: Could not load image at '{args.filepath}'. Check the path.")
            sys.exit(1)

        # Process the single image
        process_image(image)
        
        # Wait indefinitely for a key press, then close
        print("Press any key in the OpenCV window to close.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Camera Mode
    elif args.source == 'camera':
        print("Starting RealSense camera stream. Press 'q' to quit.")
        
        # Set up the realsense camera
        pipeline = rs.pipeline()
        config = rs.config()
        config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)
        
        pipeline.start(config)

        try:
            while True:
                frames = pipeline.wait_for_frames()
                color_frame = frames.get_color_frame()

                if not color_frame:
                    continue

                # Convert the RealSense frame to a numpy array and copy it
                image = np.asanyarray(color_frame.get_data()).copy()

                # Process the current frame
                process_image(image)

                # Wait 1ms for the next frame, break loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            pipeline.stop()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()