import cv2
from random import randrange

#load some pre trained data on face frontals from opencv(haar cascade algo.)
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
'''
#choose an image to detect faces in 
img=cv2.imread('dual.png')

#must convert to grayscale
grayscaled_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)
print((face_coordinates))

#Draw rectangles around the faces
#(x,y,w,h)=face_coordinates[0]
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),2)
#
cv2.imshow('MD INAMUL HASAN face detector', img)
cv2.waitKey()

print("code completed")
'''
#to capture video from webcam
webcam=cv2.VideoCapture(0)

#iterate foruer after frames
while True:
    #read the current frame
    successfull_frame_read,frame=webcam.read()
    #must convert to gryscaled
    grayscaled_img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect faces
    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)
    #print((face_coordinates))

    #Draw rectangles around the faces
    #(x,y,w,h)=face_coordinates[0]
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),2)



    cv2.imshow("MD INAMUL HASAN", frame)
    key=cv2.waitKey(1)

    #stop if q or Q is pressed
    if key==81 or key==113:
        break
#release
webcam.release()
print('code completed')
    
    













