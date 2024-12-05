import cv2
import numpy as np

# Load the video file
video_path = "/Users/skyla/Downloads/FASTEC-IL5-side_oct21_insect4_upsidedown_000004.avi"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Couldn't open the video file.")
    exit()

while True:
    # Read the next frame
    ret, frame = cap.read()
    
    if not ret:
        break  # Break the loop if the video has ended
    
    height, width = frame.shape[:2] 

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply a binary threshold to isolate the white object
    # You can adjust the threshold value depending on your video
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    
    # Perform noise removal using morphological operations (optional)
    kernel = np.ones((5, 5), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    # Find contours of the white object in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Find the largest contour (this assumes the object is the largest white shape in the frame)
        #largest_contour = min(contours, key=cv2.contourArea)
        contours = [x for x in contours if 6000 > cv2.contourArea(x) > 1000]
        sorted_contours = []
        #sorted(contours, key=cv2.contourArea, reverse=True)[3:10]
        for contour in contours:
            # Get the bounding box of the largest contour
            x, y, w, h = cv2.boundingRect(contour)
            if width*2/3 > x > width/3:
                sorted_contours.append(contour)
                # Draw the bounding box around the tracked object
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
                # Optionally, find the center of the object and draw a point
                center = (x + w // 2, y + h // 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
    output_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(output_image, sorted_contours, -1, (0, 255, 0), 2)
    # Display the result
    cv2.imshow('traced contour', output_image)
    #cv2.imshow('Tracked Object', frame)
    
    # Break the loop when the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()