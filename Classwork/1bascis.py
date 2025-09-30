import cv2
print(cv2.__version__)

#reading an image
store=cv2.imread("flower.png", cv2.IMREAD_COLOR)
cv2.imshow("screen", store)

cv2.waitKey(0)

store=cv2.imread("flower.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("screen", store)

cv2.waitKey(0)

#saving a modified image
import os
path=r"D:\ERINA\Jet Learn\VS Code OpenCV\Classwork"
img=cv2.imread("flower.png", 0)
cv2.imshow("screen", img)

cv2.waitKey(0)

os.chdir(path)
cv2.imwrite("flowergray.png", img)
print("Saved!")
