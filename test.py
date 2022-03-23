import cv2 


# read cam 
cap = cv2.VideoCapture(0)
w=int(cap.set(cv2.CAP_PROP_FRAME_WIDTH , 1920  ))
h=int(cap.set(cv2.CAP_PROP_FRAME_HEIGHT , 1080))
print("la taille " , w, h ) 
#writer= cv2.VideoWriter('video11.avi', cv2.VideoWriter_fourcc(*'XVID'), 25, (w,h))
while True : 
    _ , frame = cap.read()
    if _ : 
        print('bon' )
        #writer.write(frame)
        cv2.imwrite("img_bon223.jpg" , frame[::,::,::-1]) 
    else : print("pas bien ") 

