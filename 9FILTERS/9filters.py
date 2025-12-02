import cv2
import numpy as np

print("Try out the filters by pressing the number keys!")
print("0 - Original \n1 - Grayscale \n2 - Sepia \n3 - Negative \n4 - Cartoon \nQ - Quit")

#function for sepia filter
def sepiaFilter(frame):
   sepia=np.array([[0.272, 0.534, 0.131],
 [0.349, 0.686, 0.168],
 [0.393, 0.769, 0.189]])
   #applying on the frame
   frame_p=cv2.transform(frame, sepia)
   return np.clip(frame_p, 0, 255).astype(np.uint8)

#Opening webcam
camera=cv2.VideoCapture(0)
filter_type="Original"
while True:
   if_frame, frame_img=camera.read()
   if if_frame==False:
      break
   #applying selected filter
   if filter_type=="Grayscale":
      frame_img=cv2.cvtColor(frame_img, cv2.COLOR_BGR2GRAY)
   cv2.imshow("Filters", frame_img)
   #key event
   key=cv2.waitKey(1)
   if key==ord("0"):
      filter_type="Original"
   elif key==ord("1"):
      filter_type="Grayscale"
   elif key==ord("2"):
      filter_type="Sepia"
   elif key==ord("3"):
      filter_type="Negative"
   elif key==ord("4"):
      filter_type="Cartoon"
   elif key==ord("q"):
      break
