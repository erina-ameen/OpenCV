import cv2

forest=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\HW\3HW\forest.jpg")
resized=cv2.resize(forest, (850, 359))
cv2.imshow("Unblurred", resized)
cv2.waitKey(0)

#Gaussian Blur
blurred1=cv2.GaussianBlur(resized, (15,15), 45)
cv2.imshow("Blur 1", blurred1)
cv2.waitKey(0)

#Median Blur
blurred2=cv2.medianBlur(resized, 9)
cv2.imshow("Blur 2", blurred2)
cv2.waitKey(0)