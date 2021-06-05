import cv2 
import numpy as np
import pyautogui
import imutils


cap = cv2.VideoCapture(0)

def Press(key):
    pyautogui.press(key)

    

img1 = cv2.imread('ride.jpg')
img2 = cv2.imread('snare.png')
img4 = cv2.imread('tom1.jpg')
img1_height, img1_width, _ = img1.shape
img2 = cv2.imread('snare1.jpg')
img2_height, img2_width, _ = img2.shape
img3 = cv2.imread('hihate.jpg')
img3_height, img3_width, _ = img3.shape
img4_height, img4_width, _ = img4.shape
img5 = cv2.imread('kick.jpg')
img5_height, img5_width, _ = img5.shape
img6 = cv2.imread('tomid.jpg')
img6_height, img6_width, _ = img6.shape


#print(img4.shape)
x1 = -1 
y1 = -1
px1 = -1
py1 = -1
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    frame = imutils.resize(frame, height = 800, width= 1400)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    frame[ 0:0+img1_height , 0:0+img1_width ] = img1
    frame[ 0:0+img2_height , 400:400+img2_width ] = img2
    frame[ 0:0+img3_height , 800:800+img3_width ] = img3
    frame[ 0:0+img4_height , 1200:1200+img4_width ] = img4
    frame[ 450:450+img5_height , 0:0+img5_width ] = img5
    frame[ 450:450+img6_height , 1200:1200+img6_width ] = img6
    lower_bound_red = np.array([131,90,106])
    higher_bound_red = np.array([255,255,255])

    lower_bound_blue = np.array([40,150,166])
    higher_bound_blue = np.array([255,255,255])

    red_mask = cv2.inRange(hsv,lower_bound_red , higher_bound_red)
    blue_mask = cv2.inRange(hsv,lower_bound_blue,higher_bound_blue)

    #instruments :
    cv2.rectangle(frame , (0,0) , (200,150), (255,0,0) , 1)
    cv2.rectangle(frame , (0,450) , (200,650), (255,0,0) , 1)
    cv2.rectangle(frame , (400,0) , (600,150), (255,0,0) , 1)
    cv2.rectangle(frame , (800,0) , (1000,150), (255,0,0) , 1)
    cv2.rectangle(frame , (1200,0) , (1400,150), (255,0,0) , 1)
    cv2.rectangle(frame , (1200,450) , (1400,650), (255,0,0) , 1)
    cv2.putText(frame , 'RIDE', (70,80), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255) , 3,cv2.LINE_AA)
    contours,hierarchy = cv2.findContours(red_mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x : cv2.contourArea(x), reverse=True)
    if len(contours) > 0:
        (x1,y1,x2,y2) = cv2.boundingRect(contours[0])
        cv2.rectangle(frame,(x1,y1) , (x1+x2,y1+y2), (0,255,0),2)
        #print(x1,y1)
        if x1 > 0 and y1 > 0 and x1 < 200 and y1 < 150  and not(px1 > 0 and py1 > 0 and px1 < 200 and py1 < 150):
            Press('7')
        if x1 > 400 and y1 > 0 and x1 < 600 and y1 < 150  and not(px1 > 400 and py1 > 0 and px1 < 600 and py1 < 150):
            Press('2')
        if x1 > 800 and y1 > 0 and x1 < 1000 and y1 < 150  and not(px1 > 800 and py1 > 0 and px1 < 1000 and py1 < 150):
            Press('5')
        if x1 > 1200 and y1 > 0 and x1 < 1400 and y1 < 150  and not(px1 > 1200 and py1 > 0 and px1 < 1400 and py1 < 150):
            Press('9')
        if x1 > 0 and y1 > 450 and x1 < 200 and y1 < 650  and not(px1 > 0 and py1 > 450 and px1 < 200 and py1 < 650):
            Press('1')
        if x1 > 1200 and y1 > 450 and x1 < 1400 and y1 < 650  and not(px1 > 1200 and py1 > 450 and px1 < 1400 and py1 < 650):
            Press('w')


        px1 = x1
        py1 = y1
        

    

    # contours,hierarchy = cv2.findContours(blue_mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # contours = sorted(contours, key=lambda x : cv2.contourArea(x), reverse=True)
    # if len(contours) > 0:
    #     (x1,y1,x2,y2) = cv2.boundingRect(contours[0])
    #     cv2.rectangle(frame,(x1,y1) , (x1+x2,y1+y2), (0,255,0),2)
        #print(x1,y1)


    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == 27: 
        break
cap.release()
cv2.destroyAllWindows()
