import cv2
print(cv2.__version__)

#pink flowers image
store=cv2.imread("pinkflowers.jpg", cv2.IMREAD_COLOR)
cv2.imshow("screen", store)

cv2.waitKey(0)

store=cv2.imread("pinkflowers.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("screen", store)

cv2.waitKey(0)

#reeds image
store=cv2.imread("reeds.jpg", cv2.IMREAD_COLOR)
cv2.imshow("screen", store)

cv2.waitKey(0)

store=cv2.imread("reeds.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("screen", store)

cv2.waitKey(0)

#sea mountain image
store=cv2.imread("seamountain.png", cv2.IMREAD_COLOR)
cv2.imshow("screen", store)

cv2.waitKey(0)

store=cv2.imread("seamountain.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("screen", store)

cv2.waitKey(0)