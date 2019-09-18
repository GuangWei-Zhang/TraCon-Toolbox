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
    Counting = 0
    record = False


    while True:
        i+=1
        ret, img_raw =cap.read() #start capture images from webcam
        if ret == False:
            break
    
        img_gray = cv2.cvtColor(img_raw,cv2.COLOR_BGR2GRAY)
        y_start = 1
        y_stop = 480
        
        x_start = 1
        x_stop = 480
    #x_start_region4Counting = int(region4Counting[0])
    #x_stop_region4Counting = int(region4Counting[0]+region4Counting[2])
    
    #y_start_region4Counting = int(region4Counting[1])
    #y_stop_region4Counting = int(region4Counting[1]+region4Counting[3])
    
    #interval_step_x = (y_stop-y_start)/5 
    #interval_step_y =(x_stop-x_start)/5
    
        x_start_region4Counting = 120
        x_stop_region4Counting = 360
        
        y_start_region4Counting = 120
        y_stop_region4Counting = 360
    
    
    #img_gray = img_gray[x_start:x_stop,y_start:y_stop]

       # color_img = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)

    #cv2.imshow(r'color_img',color_img)



        #img=color_img.copy()

  # select region of interest
    #img_gray = img_gray[75:400,75:600]


        blur = cv2.GaussianBlur(img_gray,(5,5),0)
    
        retval,img_bi = cv2.threshold(blur,50,255,cv2.THRESH_BINARY_INV)
    
        binary,contours,hierarchy = cv2.findContours(img_bi.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    #for c in contours:

        #
        
        
   # cv2.drawContours(img_raw,contours+[int(y_start),int(x_start)],-1,(0,255,0),-1)

  #print(np.mean(contours))

  # only proceed if at least one contour was found
        if len(contours) > 0:
    		# find the largest contour in the mask, then use
    		# it to compute the minimum enclosing circle and
    		# centroid
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            try:
                M = cv2.moments(c)
                center = ((M["m10"] / M["m00"])+(y_start), (M["m01"] / M["m00"])+(x_start))
    
                if radius >10:
                    #cv2.circle(img_raw, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                    #cv2.circle(img_raw, center, 5, (0, 0, 255), -1)
    
                    #print('Moving_track:',Moving_track[-1][0],'Center:',center[0])
                    d_dist = hypot(Moving_track[-1][0]-center[0],Moving_track[-1][1]-center[1])
                    Speed = (d_dist/0.04)*0.075
                    #print('Delta_dist:', d_dist)
                    #d_dist =round(d_dist,2)
                    temp = "{:0>.2f}".format(Speed)
                    
                    
                    #cv2.putText(img_raw,'Speed: '+temp,(50,50),font,1,(255,255,255),2,cv2.LINE_AA)
                    #cv2.putText(img_raw,'cm/s',(280,50),font,1,(255,255,255),2,cv2.LINE_AA)
    
                    #Peak_speed = max(Peak_speed,Speed)
                    #temp2 = "{:0>.2f}".format(Peak_speed)
                    #cv2.putText(img_raw,'Peak speed: '+temp2,(50,80),font,1,(255,255,255),2,cv2.LINE_AA)
                    #cv2.putText(img_raw,'cm/s',(380,80),font,1,(255,255,255),2,cv2.LINE_AA)
    
                    #cv2.rectangle(img,(center[0]-45,center[1]-45),(center[0]+45,center[1]+45),[255,255,255],2)
                    #cv2.imshow('img_raw',img_raw)
                    #img[1:91,-91:-1] = img_raw[center[1]-45:center[1]+45,center[0]-45:center[0]+45]
    
                    Moving_track.append(center)
                    
    
                    points = np.array(Moving_track)
                    cv2.polylines(img_raw,np.int32([points[1:]]),0,(0,0,255))
                    
                    #out.write(img_raw)
                    line = str(center[0])+','+str(center[1])+','+str(Speed)+'\n'
                    
                  
                    
                    Counting_temp = (float(center[0]) > x_start_region4Counting) & (float(center[0]) < x_stop_region4Counting)  & (float(center[1]) > y_start_region4Counting) & (float(center[1]) < y_stop_region4Counting)       
                    Counting+=Counting_temp
                    #print(Counting_temp)
                    
                    
                    
                    percentage_in_region4Counting = Counting/i
                    temp_percent = "{:0>.2f}".format(percentage_in_region4Counting)
                    cv2.putText(img_raw,str(Counting_temp),(50,50),font,1,(255,0,0),2,cv2.LINE_AA)
                    #print(temp_percent)
                    cv2.rectangle(img_raw,(x_start_region4Counting,y_start_region4Counting),(x_stop_region4Counting,y_stop_region4Counting),(255,0,0))
                    cv2.imshow(r'img',img_raw)
                    out.write(img_raw)
                    
                    
                    with open(root+r'_trackTrace.csv','a') as f:
                        f.write(line)
    
    
            except ZeroDivisionError:
                print("error")
            

    #print("this is frame#:", i)


    #cv2.imshow("img",img)



        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    print(temp_percent)
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

cv2.destroyAllWindows()
out.release()
