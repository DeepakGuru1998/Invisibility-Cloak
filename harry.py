import numpy as np
import cv2
from PIL import Image

video = cv2.VideoCapture('Learn Colors With Balls _ Colours For Kids And Children _ Learning & Education For Toddlers & Babies.mp4')

ret, test_image = video.read()
ref_image = cv2.imread('shrimp.jpg')
ref_image =cv2.resize(ref_image,(720,1280))
while video.isOpened() and ret:
    
    #test_image = cv2.imread('red.jpg')
    test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110,45,45])
    upper_blue = np.array([135,255,255])
    mask_blue = cv2.inRange(test_image, lower_blue, upper_blue)
    
    image = Image.fromarray(mask_blue)
    ref_image= Image.fromarray(ref_image)
    test_image1= Image.open("red.jpg")
    image = image.convert("RGBA")
    datas = image.getdata()
    ref_datas = ref_image.getdata()
    test_datas = test_image1.getdata()
    newData = []
    x=0
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((ref_datas[x]))
        elif item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((test_datas[x]))
        else:
            newData.append(item)
        x=x+1
    
    image.putdata(newData)
    #image.show()
    open_cv_image = np.array(image) 
    # Convert RGB to BGR 
    open_cv_image = open_cv_image[:, :, ::-1].copy() 
    cv2.imshow("frame",open_cv_image)
    if cv2.waitKey(10) == 27:
        break

video.release()
cv2.destroyAllWindows()
    #cv2.waitKey()



