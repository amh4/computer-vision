import cv2

cap = cv2.VideoCapture('./DATA/hand_move.mp4')

if cap.isOpened == False:
    print('Error file not found')
    
while cap.isOpened():
    ret, frame = cap.read()
    
    if ret == True:
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    else:
        break
        
cap.release()
cv2.destroyAllWindows()