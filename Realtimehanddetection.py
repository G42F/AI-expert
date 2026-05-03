import cv2  
import numpy as np
cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error could not open your camera")
    exit()
while True:
    ret,frame=cap.read()
    if not ret:
        print("Error failed to capture image")
        break
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_skin=np.array([0,20,70],dtype=np.uint8)
    upper_skin=np.array([20,255,255],dtype=np.uint8)
    mask=cv2.inRange(hsv,lower_skin,upper_skin)
    result=cv2.bitwise_and(frame,frame,mask=mask)
    contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if contours :
        max_contours=max(contours,key=cv2.contourArea)
        if cv2.contourArea(max_contours) > 500: # Ignore small contours

# Draw the bounding box around the detected hand

            x, y, w, h = cv2.boundingRect(max_contours)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Get the center of the hand for further tracking or interaction

            center_x = int(x + w / 2)

            center_y = int(y + h / 2)

            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1) # Red dot at center

# Display the original and result frames

    cv2.imshow('Original Frame', frame)

    cv2.imshow('Filtered Frame', result)

    # Break the loop when 'q' is pressed

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

cap.release()

cv2.destroyAllWindows()

