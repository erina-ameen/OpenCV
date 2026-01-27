import cv2
import os

face_detector=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
data_set=r"D:\ERINA\Jet Learn\VS Code OpenCV\12FACE RECOGNITION\data set"
data_set_erina=r"D:\ERINA\Jet Learn\VS Code OpenCV\12FACE RECOGNITION\data set\erina"

joined_path=os.path.join(data_set, data_set_erina)

#creating a new folder that doesn't exist
if not os.path.isdir(joined_path):
    os.mkdir(joined_path)

#standard face size
(width, height)=(150, 100)
#load=cv2.CascadeClassifier(face_detector)
camera=cv2.VideoCapture(0)
counter=0
while counter<50:

    ret, frame=camera.read()
    if not ret:
        print("Frame was not read.")
        break
    gray_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_list=face_detector.detectMultiScale(gray_frame, 1.3, 4)

    #looping through each detected face
    for (x, y, width, height) in faces_list:
        cv2.rectangle(frame, (x, y), (x+width, y+height), (200,0,255), 3)
        saved_face=gray_frame[y:y+height, x:x+width]
    counter+=1

    cv2.imshow("Screen", frame)
    key=cv2.waitKey(0)

    if key==27:
        break