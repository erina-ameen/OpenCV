import cv2

bridge=cv2.imread(r"D:\ERINA\Jet Learn\VS Code OpenCV\5DRAWING ELEMENTS\bridge.jpg")

#line
start_l=(1,1)
end_l=(1000, 640)

line_colour=(255,0,255)
line_thickness=10
lined_img=cv2.line(bridge, start_l, end_l, line_colour, line_thickness)
cv2.imshow("Lined Image", lined_img)
cv2.waitKey(0)

#Rectangle
start_r=(20,20)
end_r=(200,200)

rec_colour=(255,0,255)
rec_thickness=-1
rec_img=cv2.rectangle(bridge, start_r, end_r, rec_colour, rec_thickness)
cv2.imshow("Rectangled Image", rec_img)
cv2.waitKey(0)

#Circle
start_c=(200,400)
radius=60

circle_colour=(255,0,255)
circle_thickness=1
circle_img=cv2.circle(bridge, start_c, radius, circle_colour, circle_thickness)
cv2.imshow("Circled Image", circle_img)
cv2.waitKey(0)

#Writing Text
start_t=(50,550)

txt_font=cv2.FONT_HERSHEY_COMPLEX
txt_size=3
txt_colour=(255,0,255)
txt_thickness=3
txt_img=cv2.putText(bridge, "Drawing Elements", start_t, txt_font, txt_size, txt_colour, txt_thickness, cv2.LINE_4)
cv2.imshow("Texted Image", circle_img)
cv2.waitKey(0)
