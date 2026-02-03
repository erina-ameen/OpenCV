import cv2
import numpy as np
import os

face_recognition="haarcascade_frontalface.xml"
data_set=r"D:\ERINA\Jet Learn\VS Code OpenCV\12FACE CAPTURING\dataset"

print("Make sure you are in good lighting before proceeding. ")

#creating list of imgs and corresponding names
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(data_set):
    for subdir in dirs:
        names[id]=subdir
        subject_path=os.path.join(data_set, subdir)