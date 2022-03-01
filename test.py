import cv2 


# read cam 
cap = cv2.VideoCapture(0)
#w=int(cap.set(cv2.CAP_PROP_FRAME_WIDTH , 1280 ))
#h=int(cap.set(cv2.CAP_PROP_FRAME_HEIGHT,  720))
writer= cv2.VideoWriter('video6.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, (1280,720))
while True : 
    _ , frame = cap.read()
    if _ : 
        print('bon' )
        writer.write(frame)
        #cv2.imwrite("img_bon3.jpg" , frame) 
    else : print("pas bien " ) 

