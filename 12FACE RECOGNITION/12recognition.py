import cv2
import numpy as np
import os

face_recognition='haarcascade_frontalface_default.xml'
data_set=r"D:\ERINA\Jet Learn\VS Code OpenCV\12FACE CAPTURING\dataset"

(w, h)=(150, 100)

print("Make sure you are in good lighting before proceeding. ")

#creating list of imgs and corresponding names
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(data_set):
    for subdir in dirs:
        names[id]=subdir
        subject_path=os.path.join(data_set, subdir)
        for i in os.listdir(subject_path):
            individual_path=subject_path+'/'+i
            label=id
            images.append(cv2.imread(individual_path, 0))
            labels.append(int(label))
        id+=1

(images, labels)=[np.array(lis) for lis in [images, labels]]

#model training
img_recognition_model=cv2.face.LBPHFaceRecognizer_create()
img_recognition_model.train(images, labels)
face_detector=cv2.CascadeClassifier(face_recognition)
camera=cv2.VideoCapture(0)

while True:
    (_, frame)=camera.read()
    '''if ret==False:
        print("Frame was not read.")
        break'''
    gray_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces_list=face_detector.detectMultiScale(gray_frame, 1.3, 5)

    #looping through each detected face
    for (x, y, width, height) in faces_list:
        cv2.rectangle(frame, (x, y), (x+width, y+height), (200,0,255), 3)
        saved_face=gray_frame[y:y+height, x:x+width]
        resized_face=cv2.resize(saved_face, (w, h))
        
        #predicting face
        prediction=img_recognition_model.predict(resized_face)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 3)
        if prediction[1]<500:
            cv2.putText(frame, '% s-%.0f'%(names[prediction[0]], prediction[1]), (x-10, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
        else:
            cv2.putText(frame, "Unrrecognisable",(x-10, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
    cv2.imshow("Screen", frame)
    
    key=cv2.waitKey(10)

    if key==27:
        break
