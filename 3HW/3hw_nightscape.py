import cv2

nightscape=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\HW\3HW\nightscape.jpeg")
resized=cv2.resize(nightscape, (500, 282))
cv2.imshow("Unblurred", resized)
#cv2.waitKey(0)

#Gaussian Blur
blurred1=cv2.GaussianBlur(resized, (15,13), 12)
cv2.imshow("Blur 1", blurred1)
#cv2.waitKey(0)

#Median Blur
blurred2=cv2.medianBlur(resized, 7)
cv2.imshow("Blur 2", blurred2)
cv2.waitKey(0)