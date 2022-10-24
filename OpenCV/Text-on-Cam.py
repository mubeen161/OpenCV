import cv2
vid=cv2.VideoCapture(0)
while True:
    height=int(vid.get(4))
    width=int(vid.get(3))
    rt,frame=vid.read()
    img=cv2.line(frame,(0,0),(0,0),(87,255,80),14)
    font=cv2.FONT_ITALIC
    #img=cv2.putText(img,'mohammed mubeen uddin',(100,236),font,1,(123,89,56),4)
    # #img,'text',(loc-text),font,size,(color),boldness.
   
   
    img=cv2.putText(img,'Mohammed Mubeen Uddin',(67,88),font,1,(56,12,95),6)
    cv2.imshow('mubeen',frame)
 
   
    if cv2.waitKey(1) ==ord('a'):
        break
   
vid.release()
cv2.destroyAllWindows()