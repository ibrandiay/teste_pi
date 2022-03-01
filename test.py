import cv2 


# read cam 
cap = cv2.VideoCapture(0)
w=int(cap.set(cv2.CAP_PROP_FRAME_WIDTH , 1920 ))
h=int(cap.set(cv2.CAP_PROP_FRAME_HEIGHT,  1080))
writer= cv2.VideoWriter('video5.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, (w,h))
while True : 
    _ , frame = cap.read()
    if _ : 
        print('bon' )
        writer.write(frame)
        #cv2.imwrite("img_bon3.jpg" , frame) 
    else : print("pas bien " ) 

