import cv2
import numpy as np

eyes=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\6SHAPE DETECTION\eyes.png")

#Converting to grayscale
eyes_grayscale=cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY)
eyes_grayscale_blur=cv2.blur(eyes_grayscale, (4,4))
detected_circles=cv2.HoughCircles(eyes_grayscale_blur, cv2.HOUGH_GRADIENT, 1, 20, 3, 30)

if detected_circles is not None:
    detected_circles=np.uint16(detected_circles)
    for i in detected_circles[0,:]:
        x,y,r=i[0], i[1], i[2]
        cv2.circle(eyes, (x,y), r, (0,255,0), 3)
        cv2.circle(eyes, (x,y), 1, (0,255,0), 3)
    cv2.imshow("Shape Detection", eyes)
    cv2.waitKey(0)