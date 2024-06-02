# Moving Object Detection
Moving Object Detection Using OpenCV

Moving Object Detection
Overview
This project implements a basic moving object detection system using a webcam. The system detects and highlights moving objects in the video feed using computer vision techniques such as frame differencing, Gaussian blur, and contour detection.

Prerequisites
Python 3.x
OpenCV
Git (for version control)
Installation
Clone the repository:

# How It Works
Initialization:

The script initializes the webcam and captures the first frame for background reference. It also sets up necessary variables.

Frame Processing:

Resize: The frame is resized to a width of 500 pixels for faster processing.
Grayscale Conversion: The frame is converted to grayscale to simplify the processing.
Gaussian Blur: Gaussian blur is applied to the grayscale frame to reduce noise and detail.
Background Subtraction:

The absolute difference between the initial frame and the current frame is computed to detect changes (moving objects).

Thresholding:

The difference image is thresholded to create a binary image that highlights the moving objects.

Contour Detection:

Contours are detected in the binary image. If the contour area is above a certain threshold, it is considered a moving object.

Bounding Boxes:

Bounding boxes are drawn around the detected moving objects.

Display:

The resulting frame with bounding boxes and status text is displayed.

