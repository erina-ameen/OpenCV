import cv2

video=cv2.VideoCapture('carsvid.mp4')
cars='cars.xml'
carcascade=cv2.CascadeClassifier(cars)

while True:
    ret, frame=video.read()
    if not ret:
        print("Video was not read.")
    gray_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    car_detector=carcascade.detectMultiScale(gray_frame, 1.1, 1)