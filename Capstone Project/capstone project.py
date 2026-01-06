import cv2, os
from PIL import Image

path=r"D:\ERINA\Jet Learn\VS Code OpenCV\Capstone Project\images"
os.chdir(path)
avg_width=0
avg_height=0
total_images=len(os.listdir("."))
print(total_images)

#Iterating through the Directory
for i in os.listdir("."):
    image=Image.open(os.path.join(path, i))
    new_width, new_height=image.size
    avg_width+=new_width
    avg_height+=new_height

#Calculating avg width & avg height
avg_width=avg_width//total_images
avg_height=avg_height//total_images

print(avg_width)
print(avg_height)

#Resizing and saving images
for i in os.listdir("."):
    if i.endswith(".jpg") or i. endswith (".jpeg") or i. endswith (".png"):
        image=Image.open(os.path.join(path, i))
        resized_img=image.resize((avg_width, avg_height), Image.Resampling.LANCZOS)
        resized_img.save(i, "JPEG", quality=95)
        print(i, "is resized")

#Function for video generation
def generate():
    vid_name="hobbyideas.avi"
    os.chdir(r"D:\ERINA\Jet Learn\VS Code OpenCV\Capstone Project\images")
    slide_images=[]
    for i in os.listdir("."):
        if i.endswith(".jpg") or i. endswith (".jpeg") or i. endswith (".png"):
            slide_images.append(i)
    print(slide_images)
    frame=cv2.imread(os.path.join(".", slide_images[0]))
    height, width, layers=frame.shape
    vid_store=cv2.VideoWriter(vid_name, 0, 0.5, (width, height))
    for img in slide_images:
        frame=cv2.imread(os.path.join(".", img))
        cv2.putText(frame, "Hobby Ideas", (300,500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2,cv2.LINE_AA)
        vid_store.write(frame)
    cv2.destroyAllWindows()
    vid_store.release()

generate()
