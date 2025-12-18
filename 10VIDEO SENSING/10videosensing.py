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
    x=random.randint(20, 580)
    y=random.randint(20, 420)
    radius=random.randint(20,70)
    balloon_list.append({"x":x, "y":y, "radius":radius, "popped":False})

font=cv2.FONT_HERSHEY_SIMPLEX
while True:
    frame_diff=cv2.absdiff(frame1, frame2)
    frame_diff_gray=cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)
    blurred=cv2.GaussianBlur(frame_diff_gray, (5, 5), 0)

    _,thresh=cv2.threshold(blurred, 10, 255, cv2.THRESH_BINARY)
    dilated_img=cv2.dilate(thresh, None, iterations=3)

    #finding movement
    contours, _=cv2.findContours(dilated_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    frame=frame1.copy()
    for i in balloon_list:
        if not i["popped"]:
            b=random.randint(0,255)
            g=random.randint(0,255)
            r=random.randint(0,255)
            cv2.circle(frame, [i["x"], i["y"]], i["radius"], (b,g,r), -1)
    
    #checking motion overlaps with balloon
    for c in contours:
        if cv2.contourArea(c)<1500:
            continue
    
    frame1=frame2
    tf, frame2=camera.read()

    cv2.putText(frame, "Score: "+str(score), (10,30), font, 1, (56, 32, 67), 2)

    cv2.imshow("screen", frame)

    key=cv2.waitKey(10)
    if key==27:
        break

camera.release()
cv2.destroyAllWindows()
