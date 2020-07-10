import numpy as np
import cv2

video = cv2.VideoCapture(0)
y=0
kernel = np.ones((5,5),np.uint8)

while video.isOpened():
    ret, test_image = video.read()
    if y == 0:
        ref_image=test_image
        y=y+1   
    
    test_image1 = cv2.cvtColor(test_image, cv2.COLOR_BGR2HSV)
    lower_blue1 = np.array([90,45,160])
    upper_blue1 = np.array([120,255,255])
    mask_blue1 = cv2.inRange(test_image1, lower_blue1, upper_blue1)
    lower_blue2 = np.array([40,25,40])
    upper_blue2 = np.array([110,200,255])
    mask_blue2 = cv2.inRange(test_image1, lower_blue2, upper_blue2)
    mask_blue=mask_blue1+mask_blue2

    cv2.morphologyEx(mask_blue, cv2.MORPH_CLOSE, kernel)
    mask_blue_not = cv2.bitwise_not(mask_blue)
     
    frame_1 = cv2.bitwise_and(ref_image,ref_image,mask=mask_blue)
    frame_2 = cv2.bitwise_and(test_image,test_image,mask=mask_blue_not)
    frame= cv2.addWeighted(frame_1,1,frame_2,1,0)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()



