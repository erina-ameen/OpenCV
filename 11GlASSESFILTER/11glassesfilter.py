import cv2
import numpy as np

#Loading face detector
face_detector=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
glasses1_read=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\11GlASSESFILTER\glasses1.png", cv2.IMREAD_UNCHANGED)
glasses2_read=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\11GlASSESFILTER\glasses2.png", cv2.IMREAD_UNCHANGED)
glasses3_read=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\11GlASSESFILTER\glasses3.png", cv2.IMREAD_UNCHANGED)
camera=cv2.VideoCapture(0)
filter_type="Original"
actual_h1, actual_w1=glasses1_read.shape[:2]
aspect_ratio1=actual_w1/actual_h1

print("Press keys to apply filter")
print("0 - Original")
print("1 - Glasses 1")
print("2 - Glasses 2")
print("3 - Glasses 3")
print("Esc - Quit")

#function for overlay
def overlay(bg, img, x, y):
    bg_height, bg_width=bg.shape[:2]
    img_height, img_width=img.shape[:2]
    if x+img_width>bg_width or y+img_height>bg_height:
        return bg
    transparancy=img[:,:,3]/255.0
    for i in range(3):
        bg[y:y+img_height, x:x+img_width, i]=(1-transparancy)*bg[y:y+img_height, x:x+img_width, i]+transparancy*img[:,:,i]
    return bg

while True:
    ret, frame=camera.read()
    if not ret:
        break
    if filter_type=="Glasses 1":
        grayscale=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces_list=face_detector.detectMultiScale(grayscale, 1.1, 3)
        for (x, y, width, height) in faces_list:
            glass_w=width
            glass_h=int(glass_w/aspect_ratio1)
            resized_glasses1=cv2.resize(glasses1_read, (glass_w, glass_h))
            frame=overlay(frame, resized_glasses1, x, y+70)
    if isinstance(frame, np.ndarray) and len(frame.shape)==2:
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Screen", frame)

    #setting filter according to the keys
    key=cv2.waitKey(1)
    if key==ord("0"):
        filter_type="Original"
    elif key==ord("1"):
        filter_type="Glasses 1"
    elif key==ord("2"):
        filter_type="Glasses 2"
    elif key==ord("3"):
        filter_type="Glasses 3"
    elif key==27:
        break
camera.release()
cv2.destroyAllWindows()
