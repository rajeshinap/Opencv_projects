import cv2
import numpy as np

cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("frontalEyes35x16.xml")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_face=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_face, scaleFactor=1.05, minNeighbors=8)
    eye=eye_cascade.detectMultiScale(gray_face, scaleFactor=1.05, minNeighbors=8)
    for x,y,w,h in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),3)

    for x,y,w,h in eye:
        frame=cv2.rectangle(frame,(x,y),(x+w, y+h),(0,0,255),3)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
