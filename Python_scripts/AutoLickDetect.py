#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 15:23:57 2019

@author: zhangguangwei, Li Shen
"""
from datetime import datetime
import time
import cv2
import numpy as np
#import matplotlib.pyplot as plt
import os
#from math import hypot
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename 

starttime = datetime.now()
deltaseconds = datetime.now()-starttime
deltaminutes = int(deltaseconds.total_seconds()/60) 
    
dateT = str(datetime.now().year) + str(datetime.now().month)+str(datetime.now().day) + '_'+str(datetime.now().hour)+'_'+ str(datetime.now().minute)
    
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# show an "Open" dialog box and return the path to save video file
filename = asksaveasfilename(initialdir = "/",title = "Select Save filename",filetypes = (("Video files","*.mp4"),("all files","*.*")))

(root, ext) =os.path.splitext(filename) 
font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(1)
width = int(cap.get(3))
height = int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
out = cv2.VideoWriter(filename,fourcc,30,(width,height))

while not cap.isOpened():
    cap = cv2.VideoCapture(1)
    cv2.waitKey(1000)
    print("Can't load the file")
    break

recording_dur_min=33;

while deltaminutes < recording_dur_min:
    deltaseconds = datetime.now()-starttime
    deltaminutes = int(deltaseconds.total_seconds()/60) 
    i+=1
    ret, img_raw =cap.read() #start capture images from webcam
    if ret == False:
        break
    if i==1:
        cv2.putText(img_raw, "Select Cue Zone".format((70, 70), font, 1, (255, 0, 255), 1, cv2.LINE_AA))
        r=cv2.selectROI(img_raw)
        y_start = int(r[0])
        y_stop = int(r[0]+r[2])        
        x_start = int(r[1])
        x_stop = int(r[1]+r[3])
        out_cue = cv2.VideoWriter(root + '_cue_roi.mp4', fourcc, 30, (r[2], r[3]))

        cv2.putText(img_raw, "Select Tongue Zone".format((70, 70), font, 1, (255, 0, 255), 1, cv2.LINE_AA))
        r2 = cv2.selectROI(img_raw)
        y_start2 = int(r2[0])
        y_stop2 = int(r2[0] + r2[2])
        x_start2 = int(r2[1])
        x_stop2 = int(r2[1] + r2[3])
        out_lick = cv2.VideoWriter(root + '_lick_roi.mp4', fourcc, 30, (r2[2], r2[3]))

    out.write(img_raw)
    mod = img_raw[x_start:x_stop,y_start:y_stop]
    mod2= img_raw[x_start2:x_stop2,y_start2:y_stop2]

    cue_index = np.mean(mod)
    lick_index = np.mean(mod2)

    line = str(i)+','+str(cue_index)+'\n'
    with open(root+r'_cue.csv','a') as f:
        f.write(line)
    out_cue.write(mod)

    line = str(i) + ',' + str(lick_index) + '\n'
    with open(root + r'_lick.csv', 'a') as f:
        f.write(line)
    out_lick.write(mod2)

    cv2.rectangle(img_raw,(x_start,y_start),(x_stop,y_stop),(255,0,0))
    cv2.rectangle(img_raw,(x_start2,y_start2),(x_stop2,y_stop2),(255,0,0))
    cv2.imshow(r'img',img_raw)    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
print("Processing Done!")
cv2.destroyAllWindows()
out.release()
out_cue.release()
out_lick.release()