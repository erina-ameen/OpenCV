import cv2

#img 1
img=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\HW\2HW\rgbblurcolour.jpg", 1)
b,g,r=cv2.split(img)
cv2.imshow("screen", img)
cv2.waitKey(0)

cv2.imshow("Blue Saturation", b)
cv2.waitKey(0)

cv2.imshow("Green Saturation", g)
cv2.waitKey(0)

cv2.imshow("Red Saturation", r)
cv2.waitKey(0)

#img2
img2=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\HW\2HW\umbrellacolours.jpg", 1)
b,g,r=cv2.split(img2)
cv2.imshow("screen", img2)
cv2.waitKey(0)

cv2.imshow("Blue Saturation", b)
cv2.waitKey(0)

cv2.imshow("Green Saturation", g)
cv2.waitKey(0)

cv2.imshow("Red Saturation", r)
cv2.waitKey(0)