import cv2

#Solid colour border
sunflowers=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\4BORDER\sunflowers.jpg")
bordered1=cv2.copyMakeBorder(sunflowers, 40, 40, 40, 40, cv2.BORDER_CONSTANT, value=[0,255,0])
cv2.imshow("Borderd 1", bordered1)
cv2.waitKey(0)

#Reflective border
bordered2=cv2.copyMakeBorder(sunflowers, 70, 70, 70, 70, cv2.BORDER_REFLECT, value=1)
cv2.imshow("Borderd 2", bordered2)
cv2.waitKey(0)