import cv2
print(cv2.__version__)

#reading an image
store=cv2.imread("flower.png", cv2.IMREAD_COLOR)
cv2.imshow("screen", store)

cv2.waitKey(0)

store=cv2.imread("flower.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("screen", store)

cv2.waitKey(0)