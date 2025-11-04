import cv2
import numpy as np

circles=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\6SHAPE DETECTION\circles.jpg")

#Converting to grayscale
circles_grayscale=cv2.cvtColor(circles, cv2.COLOR_BGR2GRAY)
circles_grayscale_blur=cv2.blur(circles_grayscale, (4,4))
detected_circles=cv2.HoughCircles(circles_grayscale_blur, cv2.HOUGH_GRADIENT, 1, 20, 3, 30)

if detected_circles is not None:
    detected_circles=np.uint16(detected_circles)
    for i in detected_circles[0,:]:
        x,y,r=i[0], i[1], i[2]
        cv2.circle(circles, (x,y), r, (0,255,0), 3)
        cv2.circle(circles, (x,y), 1, (0,255,0), 3)
        cv2.imshow("Shape Detection", circles)
        cv2.waitKey(0)
