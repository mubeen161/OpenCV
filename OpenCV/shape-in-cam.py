import cv2
vid=cv2.VideoCapture(0)
 
   

while True:
    height=int(vid.get(4))
    width=int(vid.get(3))
    rt,frame=vid.read()
    #img=cv2.line(frame,(0,0),(78,90),(87,255,80),15)
    #img=cv2.shape(frame,(shape placement on screeen ),(color),shape thickness)
    img=cv2.rectangle(frame,(135,450),(450,25),(255,134,90),10)
    img=cv2.circle(frame,(300,245),210,(97,45,34),10)
    img=cv2.line(frame,(height,0),(0,width),(90,78,56),10)
   
    cv2.imshow('mubeen',frame)
 
   
    if cv2.waitKey(1) ==ord('a'):
        break
   
vid.release()
cv2.destroyAllWindows()
 






