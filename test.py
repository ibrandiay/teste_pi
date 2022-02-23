import cv2 


# read cam 
cap = cv2.VideoCapture(0)
writer= cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (1200,800))
while True : 
    _ , frame = cap.read()
    if _ : 
        print('bon' )
        writer.write(frame)
        #cv2.imwrite("img.jpg" , frame) 
    else : print("pas bien " ) 

