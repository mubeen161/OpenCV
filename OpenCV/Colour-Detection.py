import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    rt,video=cap.read()
   
    img=cv2.cvtColor(video,cv2.COLOR_BGR2HSV)
    '''
    # black
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 46])
    # white
    lower_white = np.array([0, 0, 221])
    upper_white = np.array([180, 30, 255])
    #red
    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    #orange
    lower_orange = np.array([11, 43, 46])
    upper_orange = np.array([25, 255, 255])
    #yellow
    lower_yellow = np.array([26, 43, 46])
    upper_yellow = np.array([34, 255, 255])
    #green
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    #cyan
    lower_cyan = np.array([78, 43, 46])
    upper_cyan = np.array([99, 255, 255])'''
    #blue
    lower_limit=np.array([100,43,46])
    upper_limit=np.array([124,255,255])
    mask=cv2.inRange(img,lower_limit, upper_limit)
    result=cv2.bitwise_and(video,video,mask=mask)
    cv2.imshow('Tom & Jerry',result)
    if cv2.waitKey(1)==ord('a'):
        break
 
cap.release()
cv2.destroyAllWindows()
   

