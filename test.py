import cv2 


# read cam 
cap = cv2.VideoCapture(0)
while True : 
    _ , frame = cap.read()
    if _ : 
        print('bon' ) 
        cv2.imwrite("img.jpg" , cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)) 
    else : print("pas bien " ) 

