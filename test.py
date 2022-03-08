import cv2 


# read cam 
cap = cv2.VideoCapture(0)
w=int(cap.set(cv2.CAP_PROP_FRAME_WIDTH  , 1920))
h=int(cap.set(cv2.CAP_PROP_FRAME_HEIGHT , 1080 ))
print("la taille " , w, h ) 
writer= cv2.VideoWriter('video7.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, (1080,1920))
while True : 
    _ , frame = cap.read()
    if _ : 
        print('bon' )
        writer.write(frame)
        #cv2.imwrite("img_bon33.jpg" , frame) 
    else : print("pas bien " ) 

