import cv2 


# read cam 
cap = cv2.VideoCapture(0)
w=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH ))
h=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT ))
writer= cv2.VideoWriter('video1.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, (w,h))
while True : 
    _ , frame = cap.read()
    if _ : 
        print('bon' )
        writer.write(frame)
        #cv2.imwrite("img.jpg" , frame) 
    else : print("pas bien " ) 

