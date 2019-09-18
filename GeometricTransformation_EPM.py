# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 13:12:23 2018

@author: zhanglab
"""
'''Mice_tracking.py 
Written by Guang-Wei Zhang
by Oct. 16.2018
'''
'''
#installation guide
# for windows system: download and install anaconda3 
# in anaconda prompt: type in "pip install opencv-python"
# in anaconda prompt: type in "conda install -c anaconda tk"

# for mac OS, download and install anaconda3
# in terminal check default python version using: "which python", and make the anaconda as the default
# in terminal type in "pip install opencv-python"
# the tkinter comes with mac OS, no need to install again

# Usage instruction: 

Open Spyder
Drag and drop Mice_Tracking file into workspace
Hit green play button

Choose point (double click left mouse button) in the order leftUpper, RightUpper, LeftLower, RightLower
Click "c" in the keyword for confirmation
This is for two-chamber crylic transfer box, the dimension is 
_________445mm___________
|                        |
|                        |
295mm                    |
|                        |
|________________________|


fish tank
_________500mm___________
|                        |
|                        |
250mm                    |
|                        |
|________________________|

fish tank
_________480mm___________
|                        |
|                        |
|                        |
|                        |
480mm                    |
|                        |
|                        |
|                        |
|________________________|

self stim
_________250mm___________
|                        |
|                        |
180mm                    |
|                        |
|________________________|

The output video is 445 * 295 at 30fps, thus 1mm/pixel

Changes can be made, for "out" and the "pts2" for other behavior test

'''

import cv2
import numpy as np
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

box_length = 295
box_width = 295
posList = []

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img_raw,(x,y),5,(255,0,0),-1)
        mouseX,mouseY = x,y
        posList.append((x, y))
        print(posList)


#def onMouse(event, x, y, flags, param):
 #  global posList
  # if event == cv2.EVENT_LBUTTONDOWN:
   #     posList.append((x, y))
#cv2.setMouseCallback('WindowName', onMouse)


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)
(root, ext) =os.path.splitext(filename) 

duration = 1  # second
freq = 440  # Hz

#mouse_cascade = cv2.CascadeClassifier('mouse_body_cascade.xml')
cap = cv2.VideoCapture(filename)

Moving_track = [(0,0)]
## add text
font = cv2.FONT_HERSHEY_SIMPLEX

# export video setting
width = int(cap.get(3))
height = int(cap.get(4))


fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
out = cv2.VideoWriter(root+'_GeometricallyTransformed.mp4',fourcc,30,(box_length,box_width))





Peak_speed = 0


while not cap.isOpened():
    cap = cv2.VideoCapture(filename)
    cv2.waitKey(1000)
    #os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
    print("Can't load the file")
    break
# pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)

a=[(0,0)]
i=0
record = False


while True:
    i+=1
    ret, img_raw =cap.read() #start capture images from webcam
    if ret == False:
        break
  ####
    
  ####
        
  #if i==1:
   #     img_ROI = img_raw.copy()
    #    cv2.imshow(r'ROI',img_ROI)


        
    while i==1:
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", draw_circle)
#r = cv2.selectROI(img_raw)
        posNp = np.array(posList) 
        cv2.imshow('image',img_raw)
        k = cv2.waitKey(20) & 0xFF
        if k == ord("r"):
            image = img_raw
        if k == ord("c"):
            break
        #elif k == ord('a'):
         #   print mouseX,mouseY
    
    img_gray = cv2.cvtColor(img_raw,cv2.COLOR_BGR2GRAY)

    img = img_raw
    rows,cols,ch = img.shape
    pts1 = np.float32(posList)
    pts2 = np.float32([[0,0],[box_length,0],[0,box_width],[box_length,box_width]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(img,M,(box_length,box_width))
    cv2.imshow('input',img)
    cv2.imshow('output',dst)
    out.write(dst)
    print("this is frame#:", i)


    #cv2.imshow("img",img)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      # i+=1

      # only proceed if the radius meets a minimum size
    #if radius > 10:
      # draw the circle and centroid on the frame,
      # then update the list of tracked points
   #      cv2.circle(img, (int(x), int(y)), int(radius),
    #     (0, 255, 255), 2)
    #     cv2.circle(img, center, 5, (0, 0, 255), -1)


     #cv2.imshow("img",img)



print("Processing Done!")
cap.release()
cv2.destroyAllWindows()
out.release()



