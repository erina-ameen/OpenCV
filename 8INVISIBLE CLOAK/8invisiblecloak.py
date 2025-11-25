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
    #lower red
    lower_r=np.array([0, 120, 70])
    upper_r=np.array([10, 255, 255])
    mask1=cv2.inRange(converted_frame, lower_r, upper_r)
    #darker red
    lower_r2=np.array([170, 120, 70])
    upper_r2=np.array([1800, 255, 250])
    mask2=cv2.inRange(converted_frame, lower_r2, upper_r2)
    #combining the masks
    combo_mask=mask1+mask2
    #cleaning the mask
    combo_mask=cv2.morphologyEx(combo_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=3)
    combo_mask=cv2.dilate(combo_mask, np.ones((3,3), np.uint8), iterations=2)
    inverted_mask=cv2.bitwise_not(combo_mask)
    #replacing red area with the curtain background
    result_mask1=cv2.bitwise_and(bg, bg, mask=combo_mask)
    result_mask2=cv2.bitwise_and(frame, frame, mask=inverted_mask)
    final_result=cv2.addWeighted(result_mask1, 1, result_mask2, 1, 0)
    cv2.imshow("Invisible MASK", final_result)
    if cv2.waitKey(10)==27:
        break
raw.release()
cv2.destroyAllWindows()
