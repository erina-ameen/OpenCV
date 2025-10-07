import cv2

scenery=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\3ARITHMETICS\scenery.jpg")
resized=cv2.resize(scenery, (1000, 580))
cv2.imshow("Unblurred", resized)
#cv2.waitKey(0)

#Gaussian Blur
blurred1=cv2.GaussianBlur(resized, (15,15), 10)
cv2.imshow("Blur 1", blurred1)
#cv2.waitKey(0)

#Median Blur
blurred2=cv2.medianBlur(resized, 5)
cv2.imshow("Blur 2", blurred2)
cv2.waitKey(0)