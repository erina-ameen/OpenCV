import cv2
import random
import numpy as np

camera=cv2.VideoCapture(0)
tf, frame1=camera.read()
tf, frame2=camera.read()
balloon_list=[]
balloon_num=10
score=0

for i in range(balloon_num):
    x=random.randint(0, 500)
    y=random.randint(0, 500)
    radius=random.randint(20-70)
    balloon_list.append({"x":x, "y":y, "radius":radius, "popped":False})

font=cv2.FONT_HERSHEY_SIMPLEX
while True:
    frame_diff=cv2.absdiff(frame1, frame2)
    frame_diff_gray=cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)
    blurred=cv2.GaussianBlur(frame_diff_gray, (5, 5), 0)

    _,thresh=cv2.threshold(blurred, 10, 255, cv2.THRESH_BINARY)
    dilated_img=cv2.dilate(thresh, None, iterations=3)