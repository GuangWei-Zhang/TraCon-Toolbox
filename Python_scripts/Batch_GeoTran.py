# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:03:30 2018

@author: zhanglab
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 13:03:03 2018

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
Select downsampled video file (recommend 480p x 480p for faster speed)
Once finished, video with tracking trace and excel sheet appear in source folder for video
For excel file: three columns, first is x, second is y coord, third is pixel distance traveled between frames
For the third column, value is always incorrect, so change to zero.
Plot x and y columns for trace of motion graph (line graph)
Plot motion column for speed trace. Convert y-axis to inches per frame by measure how many pixels per inch in video (and convert speed to secs using 30 fps conversion).

Delete orginal excel file for a given video if you want to re-run the program analysis for the same video (it will just add data to the original excel file making it really long).
'''
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

two-chamber place preference
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

water sink tank
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

Cross Maze Test


610 x 610 mm
            _ 
           | |
           | |
           | |
___________| |___________   
|__________   ___________| 
           | |
           | |                                                                                             
           | |
           |_|
           

water_searching_form_board

_________640mm___________
|                        |
|                        |
430mm                    |
|                        |
|________________________|


homeCage
_________280mm___________
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
#import matplotlib.pyplot as plt
import os
from math import hypot
from tkinter import Tk

from tkinter.filedialog import askopenfilenames
#import os


box_length = 480
box_width = 480

posList = []

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img_raw,(x,y),1,(255,0,0),-1)
        mouseX,mouseY = x,y
        posList.append((x, y))
        print(posList)




root1 = Tk()
filez = askopenfilenames(parent = root1, title = 'Choose file')



fourcc = cv2.VideoWriter_fourcc('m','p','4','v')

#print(root1.tk.splitlist(filez))

for fullFileName in root1.tk.splitlist(filez):
    filename = fullFileName
    (root, ext) =os.path.splitext(filename) 
    duration = 1  # second
    freq = 440  # Hz
   
    cap = cv2.VideoCapture(filename)
    
    ## add text

    
    # export video setting

    i=0
    while i<2:
        i+=1
        ret, img_raw =cap.read() #start capture images from webcam
        if ret == False:
            break
    
        while i==1:
            cv2.namedWindow("image")
            cv2.setMouseCallback("image", draw_circle)
            posNp = np.array(posList) 
            cv2.imshow('image',img_raw)
            k = cv2.waitKey(20) & 0xFF
            if k == ord("r"):                                                                                                                                                                                            
                image = img_raw
            if k == ord("c"):
                break
 
    cap.release()
    
cv2.destroyAllWindows()       
        #print(posNp)

j=0
for fullFileName in root1.tk.splitlist(filez):
    j+=1
    filename = fullFileName
    print(filename)
    (root, ext) =os.path.splitext(filename) 
    cap = cv2.VideoCapture(filename)
    while not cap.isOpened():
        cap = cv2.VideoCapture(filename)
        cv2.waitKey(1000)
        #os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
        print("Can't load the file")
        break
    duration = 1  # second
    freq = 440  # Hz
   
    cap = cv2.VideoCapture(filename)
    width = int(cap.get(3))
    height = int(cap.get(4))


    font = cv2.FONT_HERSHEY_SIMPLEX
    out = cv2.VideoWriter(root+'_GeometricallyTransformed_1.mp4',fourcc,30,(box_length,box_width))
    while True:
        ret, img_raw =cap.read() #start capture images from webcam
        if ret == False:
            break
        #img_gray = cv2.cvtColor(img_raw,cv2.COLOR_BGR2GRAY)

        #img = cv2.cvtColor(img_gray,cv2.COLOR_GRAY2BGR)
        img = img_raw
        rows,cols,ch = img.shape
        pts1 = np.float32(posList[(j-1)*4:(j*4)])
        pts2 = np.float32([[0,0],[box_length,0],[0,box_width],[box_length,box_width]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        dst = cv2.warpPerspective(img,M,(box_length,box_width))
        #cv2.imshow('input',img)
        cv2.imshow('output',dst)
        out.write(dst)
        #print("this is frame#:", i)
          
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()



#cap.release()
#cv2.destroyAllWindows()