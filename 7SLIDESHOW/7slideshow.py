import cv2, os
from PIL import Image

path=r"D:\ERINA\Jet Learn\VS Code OpenCV\7SLIDESHOW\images"
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
    if i.endswith((".jpg",".jpeg",".png")):
        image=Image.open(os.path.join(path, i))
        resized_img=image.resize((avg_width, avg_height), Image.Resampling.LANCZOS)
        resized_img.save(i, "JPEG", quality=95)
        print(i, "is resized")