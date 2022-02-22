import cv2 


# read cam 
cap = cv2.VideoCapture(0)
while True : 
    _ , frame = cap.read()
    if _ : 
        print('bon' ) 
        cv2.imwrite("img.jpg" , frame[::-1] ) 
    else : print("pas bien " ) 

