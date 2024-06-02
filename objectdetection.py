import cv2  # For image processing
import time  # For introducing delays

# Initialize the webcam
cam = cv2.VideoCapture(0)  # 0 is the ID of the default camera
time.sleep(1)  # Allow the camera to warm up

firstFrame = None  # To store the initial frame for background reference
area = 500  # Minimum area to consider for detecting a moving object

while True:
    # Read a frame from the camera
    _, img = cam.read()
    text = "Normal"
    
    # Resize the frame to a width of 500 pixels for faster processing
    img = cv2.resize(img, (500, int(img.shape[0] * 500 / img.shape[1])))
    
    # Convert the frame to grayscale
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to the grayscale frame
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)
    
    # Capture the first frame
    if firstFrame is None:
        firstFrame = gaussianImg
        continue

    # Compute the absolute difference between the first frame and the current frame
    imgDiff = cv2.absdiff(firstFrame, gaussianImg)
    
    # Apply thresholding to get a binary image
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
    
    # Dilate the thresholded image to fill in holes
    threshImg = cv2.dilate(threshImg, None, iterations=2)
    
    # Find contours in the thresholded image
    cnts, _ = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Loop over the contours
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue  # Ignore small contours
        
        # Compute the bounding box for the contour
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving Object detected"
    
    # Print the status text
    print(text)
    
    # Draw the text on the frame
    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    # Display the frame with the detections
    cv2.imshow("cameraFeed", img)
    
    # Break the loop if the 'q' key is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
