import cv2
import time
import numpy as np

raw=cv2.VideoCapture(r"D:\ERINA\Jet Learn\VS Code OpenCV\8INVISIBLE CLOAK\video.mp4")
if not raw.isOpened():
    print("File is not accessible.")
    exit()
time.sleep(2)

frame_counter=0
bg=None

#Capturing the background
for i in range(60):
    return_vid, frame = raw.read()
    if return_vid==False:
        print("This frame was not detected. It has been skipped.")
        continue
    bg=frame

if bg is None:
    print("Error. Please open video.")
    exit()

#Flipping the background image
bg=np.flip(bg, axis=1)

#Invisibility effect]
while raw.isOpened():
    return_vid, frame = raw.read()
    if return_vid==False:
        break
    frame_counter+=1
    frame=np.flip(frame, axis=1)
    converted_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Range for red colour
    lower_r=np.array([0, 125, 60])
    upper_r=np.array([10, 255, 255])
    mask1=cv2.inRange(converted_frame, lower_r, upper_r)
    #darker red
    lower_r2=np.array([180, 125, 60])
    upper_r2=np.array([200, 125, 60])
    mask2=cv2.inRange(converted_frame, lower_r2, upper_r2)