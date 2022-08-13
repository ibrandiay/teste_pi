import cv2 
import numpy as np

# read cam 
cap = cv2.VideoCapture(0)
print("la taille " , w, h ) 
#writer= cv2.VideoWriter('video15.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (640,480))
while True : 
    _ , frame = cap.read()
    if _ : 
        print('new modif')
        print('bon' )
        #writer.write(frame)
        cv2.imwrite("img1.jpg" , frame[::,::,::-1]) 
        cv2.read
        ____________
    else : print("pas bien ") 

