#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:49:56 2018

@author: zhangguangwei
"""

import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
import os
import matplotlib.pyplot as plt

from scipy import signal




root = Tk()
filez = askopenfilenames(parent = root, title = 'Choose a file')

print(root.tk.splitlist(filez))

for fullFileName in root.tk.splitlist(filez):
    print(fullFileName)
    (root, ext) =os.path.splitext(fullFileName) 
    data=[]
    data = pd.read_csv(fullFileName,sep='\t',header = 0)
    data.columns=['calSig','trigger','NaN']
    
    fig = plt.figure()
    ax1 = plt.subplot(211)
    ax1.plot(data.calSig,label ='Calcium Signal',linewidth = 0.25)
    ax1.set_ylabel("CalSig(V)")
    
    Cal_resampled = signal.resample(data.calSig,25)
    #this uses FFT to resample the 1-D data
    
    ax2 = plt.subplot(212)
    ax2.plot(data.trigger,label = 'TriggerChannel',linewidth =0.25)
    ax2.set_ylabel('Trig(V)')
    
    plt.show()
    fig.savefig(root+r"_CalSig&Trigger.pdf", bbox_inches='tight')
