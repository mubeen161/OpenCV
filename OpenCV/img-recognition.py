import cv2
img=cv2.imread('C:/Users/mohammed mubeen uddi/OneDrive/Desktop/my programs/python/image.jpeg',0)
 
 
cv2.imshow('foottball',img)
 
 
ball=cv2.imread('C:/Users/mohammed mubeen uddi/OneDrive/Desktop/my programs/python/image2.jpeg',0)
img=cv2.resize(img,(0,0),fx=0.7,fy=0.7)
ball=cv2.resize(ball,(0,0),fx=0.7,fy=0.7)
h,w=ball.shape
methods = [cv2.TM_SQDIFF_NORMED, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]#method-3,4 are not accurate
for method in methods:
    img2=img.copy()
    result=cv2.matchTemplate(img2,ball,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in[cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location= min_loc
    else:
        location=max_loc
bottom_right=(location[0]+ w, location[1]+h)
cv2.rectangle((img2),location,bottom_right,255,5)
 
cv2.imshow('result', img2)
 
 
cv2.imshow('ball',ball)
cv2.waitKey(0)
cv2.destroyAllWindows()
