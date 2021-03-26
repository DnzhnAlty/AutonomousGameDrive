import cv2
import numpy as np
import math

def canny(image):

    blur=cv2.GaussianBlur(image,(3,3),1)
    canny=cv2.Canny(blur,90,120)
    dilate=cv2.dilate(canny,(5,5),iterations=1)
    erode=cv2.erode(dilate,(5,5),iterations=1)
    filterResult=colorFilter(image)
    #combinedImage = cv2.bitwise_or(filterResult, erode)
    combinedImage=filterResult
    return canny,dilate,erode,combinedImage

def colorFilter(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower_road = np.array([0, 0, 0])
    upper_road = np.array([255, 47, 119])

    road = cv2.inRange(hsv, lower_road, upper_road)  ## Karma renk.
    #cv2.imshow("Yol",yol)

    FinalImage = road

    return FinalImage

def LinesDetector(img,Height,Width):


    for x_left in range(int(Width)//2,-1,-1):

        if (img[325,x_left]==0):
            #print("Sol nokta =", x_sol)
            break
        if (x_left<1):
            x_left = 0
            #print("Sol nokta =", x_sol)
            break

    for x_right in range(int(Width)//2,Width,1):
        #print("\n", x_sag)
        if (img[325,x_right]==0):
            #print("Sağ nokta =",x_sag)
            break
        if  (x_right>Width-2):
            x_right= Width-1
            #print("Sağ nokta =",x_sag)
            break


    return x_left,x_right

def LineLenghtCalculator (p1_x,p1_y,p2_x,p2_y):
    a= math.sqrt((p1_x - p2_x) ** 2 + (p1_y - p2_y) ** 2)
    return a
