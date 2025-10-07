import cv2
import numpy as np

#adding two images
image1=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\3ARITHMETICS\image1.jpg")
image2=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\3ARITHMETICS\image2.jpg")

image_mix=cv2.addWeighted(image1, 0.8, image2, 0.8, 0)
cv2.imshow("screen", image_mix)
cv2.waitKey(0)

#subtracting images
img1=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\3ARITHMETICS\img1.jpg")
img2=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\3ARITHMETICS\img2.jpg")

img_subtract=cv2.subtract(img1, img2)
cv2.imshow("screen", img_subtract)
cv2.waitKey(0)

#resizing images
flower=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\3ARITHMETICS\flower.png")
cv2.imshow("screen", flower)
cv2.waitKey(0)

resizedflower=cv2.resize(flower, (300, 300))
cv2.imshow("screen", resizedflower)
cv2.waitKey(0)

#erosion
cv2.imshow("screen", image1)
cv2.waitKey(0)
kernel=np.ones((5,5), np.uint8)
eroded=cv2.erode(image1, kernel)
cv2.imshow("screen", eroded)
cv2.waitKey(0)