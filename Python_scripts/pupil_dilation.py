# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 13:34:51 2019

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


import cv2
import numpy as np
#import matplotlib.pyplot as plt
import os
from math import hypot
from tkinter import Tk

from tkinter.filedialog import askopenfilenames
#import os





root1 = Tk()
filez = askopenfilenames(parent = root1, title = 'Choose file')

#print(root1.tk.splitlist(filez))

for fullFileName in root1.tk.splitlist(filez):
    filename = fullFileName
    (root, ext) =os.path.splitext(filename) 
    print(root)
    
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
    out = cv2.VideoWriter(root+'_out_half_widthCenterOFT.mp4',fourcc,30,(width,height))





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
    
    # here i represent the frame number 
    Counting = 0
    record = False


    while True:
        i+=1
        ret, img_raw =cap.read() #start capture images from webcam
        if ret == False:
            break
    
        img_gray = cv2.cvtColor(img_raw,cv2.COLOR_BGR2GRAY)
        

        color_img = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)

        cv2.imshow(r'color_img',color_img)



        #img=color_img.copy()

  # select region of interest
    #img_gray = img_gray[75:400,75:600]


        blur = cv2.GaussianBlur(img_gray,(5,5),0)
    
        retval,img_bi = cv2.threshold(blur,100,255,cv2.THRESH_BINARY_INV)
        
        cv2.imshow(r'img_bi',img_bi)
    
        binary,contours,hierarchy = cv2.findContours(img_bi.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        #for c in contours:
            #cv2.drawContours(img_raw,contours+[int(y_start),int(x_start)],-1,(0,255,0),-1)

  #print(np.mean(contours))

  # only proceed if at least one contour was found
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            try:
                M = cv2.moments(c)
                center = ((M["m10"] / M["m00"]), (M["m01"] / M["m00"]))
    
                if radius >5:
                    cv2.circle(img_raw, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                    temp = "{:0>.2f}".format(radius) 
                    Moving_track.append(center)
                    points = np.array(Moving_track)
                    cv2.polylines(img_raw,np.int32([points[1:]]),0,(0,0,255))
                    line = str(str(radius)+'\n')
                    cv2.imshow(r'img',img_raw)
                    out.write(img_raw)
                    with open(root+r'_trackTrace.csv','a') as f:
                        f.write(line)
                else:
                    line = str('0'+'\n')
                    with open(root+r'_trackTrace.csv','a') as f:
                        f.write(line)
                        print("empty frame")

                        
            except ZeroDivisionError:
                line = str('0'+'\n')
                with open(root+r'_trackTrace.csv','a') as f:
                    f.write(line)
                print("error")
                
                                
        else:
            line = str('0'+'\n')
            with open(root+r'_trackTrace.csv','a') as f:
                f.write(line)
                print("empty frame")



        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()




print("Processing Done!")

cv2.destroyAllWindows()
out.release()



















