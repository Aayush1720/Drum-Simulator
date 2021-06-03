import cv2 
import numpy as np
import pyautogui
import imutils


cap = cv2.VideoCapture(0)

def Press(key):
    pyautogui.press(key)

img = cv2.imread('ride1.jpg')
img_height, img_width, _ = img.shape

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    frame = imutils.resize(frame, height = 800, width= 1400)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    frame[ 0:0+img_height , 0:0+img_width ] = img
    lower_bound_red = np.array([131,90,106])
    higher_bound_red = np.array([255,255,255])

    lower_bound_blue = np.array([40,150,166])
    higher_bound_blue = np.array([255,255,255])

    red_mask = cv2.inRange(hsv,lower_bound_red , higher_bound_red)
    blue_mask = cv2.inRange(hsv,lower_bound_blue,higher_bound_blue)

    #instruments :
    cv2.rectangle(frame , (0,0) , (200,150), (255,0,0) , 1)
    cv2.putText(frame , 'RIDE', (70,80), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255) , 3,cv2.LINE_AA)
    contours,hierarchy = cv2.findContours(red_mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x : cv2.contourArea(x), reverse=True)
    if len(contours) > 0:
        (x1,y1,x2,y2) = cv2.boundingRect(contours[0])
        cv2.rectangle(frame,(x1,y1) , (x1+x2,y1+y2), (0,255,0),2)
        print(x1,y1)
        if x1 > 0 and y1 > 0 and x1 < 200 and y1 < 150:
            Press('7')

    

    contours,hierarchy = cv2.findContours(blue_mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x : cv2.contourArea(x), reverse=True)
    if len(contours) > 0:
        (x1,y1,x2,y2) = cv2.boundingRect(contours[0])
        cv2.rectangle(frame,(x1,y1) , (x1+x2,y1+y2), (0,255,0),2)
        print(x1,y1)


    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == 27: 
        break
cap.release()
cv2.destroyAllWindows()
