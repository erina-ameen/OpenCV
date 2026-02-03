import cv2
import os

face_detector=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
data_set=r"D:\ERINA\Jet Learn\VS Code OpenCV\12FACE RECOGNITION\data set"
#data_set_erina=r"D:\ERINA\Jet Learn\VS Code OpenCV\12FACE RECOGNITION\data set\erina"

joined_path=os.path.join(data_set, "erina")

#creating a new folder that doesn't exist
if not os.path.isdir(joined_path):
    os.mkdir(joined_path)

#standard face size
(width, height)=(150, 100)
#load=cv2.CascadeClassifier(face_detector)
camera=cv2.VideoCapture(0)
counter=0
while counter<30:
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
        resized_face=cv2.resize(saved_face, (width, height))
        print("Hello")
        cv2.imwrite(f"{joined_path}/{counter}.png", resized_face)
        print("Hello2")
        counter+=1

    cv2.imshow("Screen", frame)
    key=cv2.waitKey(1)

    if key==27:
        break

camera.release()
cv2.destroyAllWindows()

print("Photos captured.")
