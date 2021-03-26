import numpy as np
from PIL import ImageGrab
import cv2
import time
import Settings as stng
import threading as thread
from directkeys import ReleaseKey, PressKey, W,A,S,D
from GameXml import ReadXML, WriteXML

Height=490
Width=640

leftLineLenght=15
rightLineLenght=15

fileName="LenghtDatabase"

### Screen record code.
def screen_record():
    last_time = time.time()
    while(True):

        printscreen =  np.array(ImageGrab.grab(bbox=(0,50,Width,Height+50)))
        #print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()

        copy_frame=np.copy(printscreen)         ## Ekran alıntısını kopyaladık.

        copy_canny,copy_dilate,copy_erode,copy_combinedImage=stng.canny(copy_frame)     ## Combine halini aldık.


        # plt.imshow(copy_combinedImage)

        #print(copy_combinedImage.shape)

        x_left,x_right=stng.LinesDetector(copy_combinedImage,Height,Width)

        leftLineLenght = stng.LineLenghtCalculator(x_left, 325, Width//2, Height)
        rightLineLenght = stng.LineLenghtCalculator(x_right, 325, Width//2, Height)

        WriteXML(fileName,leftLineLenght,rightLineLenght)

        LineDrawer(copy_frame,x_left,x_right)

        cv2.imshow("Screen",copy_frame)
        cv2.imshow("Combined",copy_combinedImage)
        # plt.show()
        if cv2.waitKey(20) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


def LineDrawer(frame,left,right):

    cv2.line(frame, (Width//2,Height), (left, 325), (0, 255, 0), thickness=2)
    cv2.line(frame, (Width//2,Height),(right,325), (0, 255, 0), thickness=2)

def CarController ():
    while(True):

        leftAmount,rightAmount=ReadXML(fileName)

        if(float(leftAmount)>float(rightAmount)):
             print("Left")
             PressKey(A)
             #time.sleep(1/(float(rightAmount)//float(leftAmount)))
             time.sleep(0.2)
             ReleaseKey(A)
             time.sleep(0.27)

        if(float(leftAmount))<float(rightAmount):
            print("Right")
            PressKey(D)
            #time.sleep(1/(float(leftAmount)//float(rightAmount)))
            time.sleep(0.2)
            ReleaseKey(D)
            time.sleep(0.27)

def CarForwardMover ():
    while (True):
        PressKey(W)
        time.sleep(0.10)
        ReleaseKey(W)
        time.sleep(0.20)
        print("Forward")

def Waiter():
    PressKey(S)
    time.sleep(0.2)
    ReleaseKey(S)

if __name__ == '__main__':
    time.sleep(3)
    p1= thread.Thread(target =screen_record)
    p2= thread.Thread(target =CarController)
    p3= thread.Thread(target =CarForwardMover)

    p1.start()

    p2.start()

    p3.start()

