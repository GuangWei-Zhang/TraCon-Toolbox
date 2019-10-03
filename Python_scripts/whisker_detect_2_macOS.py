# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 20:17:02 2018

@author: zhanglab
"""
'''
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('example.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x,y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs,ys)
    
ani = animation.FuncAnimation(fig,animate,interval =1000)

'''






import numpy as np
import cv2
#from tkinter import Tk
#from tkinter.filedialog import askopenfilename
from Tkinter import Tk
from tkFileDialog import askopenfilename
import os

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)
(root, ext) =os.path.splitext(filename) 

duration = 1  # second
freq = 440  # Hz

#mouse_cascade = cv2.CascadeClassifier('mouse_body_cascade.xml')
cap = cv2.VideoCapture(filename)


sdThresh = 10
font = cv2.FONT_HERSHEY_SIMPLEX
#TODO: Face Detection 1

def distMap(frame1, frame2):
    """outputs pythagorean distance between two frames"""
    frame1_32 = np.float32(frame1)
    frame2_32 = np.float32(frame2)
    diff32 = frame1_32 - frame2_32
    norm32 = np.sqrt(diff32[:,:,0]**2 + diff32[:,:,1]**2 + diff32[:,:,2]**2)/np.sqrt(255**2 + 255**2 + 255**2)
    dist = np.uint8(norm32*255)
    return dist

cv2.namedWindow('frame')
cv2.namedWindow('dist')

#capture video stream from camera source. 0 refers to first camera, 1 referes to 2nd and so on.
#cap = cv2.VideoCapture(0)

_, frame1 = cap.read()
_, frame2 = cap.read()

facecount = 0
i=0;
while(True):
     
    _, frame3 = cap.read()
    i+=1
    if i==1:
        r = cv2.selectROI(frame3)
    
    #img_gray = cv2.cvtColor(frame3,cv2.COLOR_BGR2GRAY)
        y_start = int(r[0])
        y_stop = int(r[0]+r[2])
        
        x_start = int(r[1])
        x_stop = int(r[1]+r[3])
     
    
    #frame3 = img_gray
    
    rows, cols, _ = np.shape(frame3)
    cv2.imshow('dist', frame3[x_start:x_stop,y_start:y_stop])
    dist = distMap(frame1[x_start:x_stop,y_start:y_stop], frame3[x_start:x_stop,y_start:y_stop])

    frame1 = frame2
    frame2 = frame3

    # apply Gaussian smoothing
    mod = cv2.GaussianBlur(dist, (9,9), 0)
    whisker_index = np.sum(mod)
    # apply thresholding
    _, thresh = cv2.threshold(mod, 100, 255, 0)

    # calculate st dev test
    _, stDev = cv2.meanStdDev(mod)

    cv2.imshow('dist', mod)
    cv2.putText(frame2, "Standard Deviation - {}".format(round(stDev[0][0],0)), (70, 70), font, 1, (255, 0, 255), 1, cv2.LINE_AA)
    if stDev > sdThresh:
            print("Motion detected.. Do something!!!");
            #TODO: Face Detection 2

    cv2.imshow('frame', frame2)
    
    line = str(i)+','+str(whisker_index)+','+str(stDev)+'\n'
    with open(root+r'_whisker.csv','a') as f:
        f.write(line)
        
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
