import cv2
vid=cv2.VideoCapture(0)
while True:
    rt,video=vid.read()
    cv2.imshow('frame',video)
 
    if cv2.waitKey(1)==ord('a'):
        break