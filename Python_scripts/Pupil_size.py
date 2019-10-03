#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 21:05:48 2018

@author: zhangguangwei
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


import cv2
import numpy as np
#import matplotlib.pyplot as plt
import os
from math import hypot
from tkinter import Tk
from tkinter.filedialog import askopenfilename



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
out = cv2.VideoWriter(root+'_out.mp4',fourcc,30,(width,height))





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
        
        
    if i==1:
        r = cv2.selectROI(img_raw)
    
    img_gray = cv2.cvtColor(img_raw,cv2.COLOR_BGR2GRAY)
    y_start = int(r[0])
    y_stop = int(r[0]+r[2])
    
    x_start = int(r[1])
    x_stop = int(r[1]+r[3])
     
    
    img_gray = img_gray[x_start:x_stop,y_start:y_stop]

    color_img = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)

    #cv2.imshow(r'color_img',color_img)



    img=color_img.copy()

  # select region of interest
    #img_gray = img_gray[75:400,75:600]


    blur = cv2.GaussianBlur(img_gray,(5,5),0)

    retval,img_bi = cv2.threshold(blur,50,255,cv2.THRESH_BINARY_INV)

    binary,contours,hierarchy = cv2.findContours(img_bi.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    pupil_size = np.sum(contours)
    
    cv2.putText(img_raw,'Speed: '+temp,(50,50),font,1,(255,255,255),2,cv2.LINE_AA)

    cv2.imshow("img",img)
    
    c = max(contours, key=cv2.contourArea)
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    try:
            M = cv2.moments(c)
    #for c in contours:

        #
        
        
   # cv2.drawContours(img_raw,contours+[int(y_start),int(x_start)],-1,(0,255,0),-1)

  #print(np.mean(contours))


print("Processing Done!")
cap.release()
cv2.destroyAllWindows()
out.release()
