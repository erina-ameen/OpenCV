import cv2

img=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\2SATURATION\rgbcolormodel.png", 1)
b,g,r=cv2.split(img)
cv2.imshow("screen", img)
cv2.waitKey(0)

cv2.imshow("Blue Saturation", b)
cv2.waitKey(0)

cv2.imshow("Green Saturation", g)
cv2.waitKey(0)

cv2.imshow("Red Saturation", r)
cv2.waitKey(0)