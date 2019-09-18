import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from math import hypot

duration = 1  # second
freq = 440  # Hz

path = "/Users/zhangguangwei/Dropbox/MS_Supp_video/20hz_demo.mov"
#mouse_cascade = cv2.CascadeClassifier('mouse_body_cascade.xml')
cap = cv2.VideoCapture(path)

Moving_track = [(0,0)]
## add text
font = cv2.FONT_HERSHEY_SIMPLEX

# export video setting
#width = cap.get(3)
#height = cap.get(4)

video_name = '/users/zhangguangwei/desktop/VGluT2_speed_test'
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
out = cv2.VideoWriter(video_name+'.mp4',fourcc,30,(640,360))

Peak_speed = 0


while not cap.isOpened():
    cap = cv2.VideoCapture(path)
    cv2.waitKey(1000)
    #os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
    print("Can't load the file")

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
    #img = img_raw[:,:,1]
  ####

    img_gray = cv2.cvtColor(img_raw,cv2.COLOR_BGR2GRAY)

    color_img = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)

    #cv2.imshow('color_img',color_img)



    img=color_img.copy()

  # select region of interest
    #img_gray = img_gray[75:400,75:600]


    blur = cv2.GaussianBlur(img_gray,(5,5),0)

    retval,img_bi = cv2.threshold(blur,20,255,cv2.THRESH_BINARY_INV)

    binary,contours,hierarchy = cv2.findContours(img_bi.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:

        cv2.drawContours(img,contours,-1,(0,255,0),-1)

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
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))


            if radius >10:
                cv2.circle(img, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(img, center, 5, (0, 0, 255), -1)

                #print('Moving_track:',Moving_track[-1][0],'Center:',center[0])
                d_dist = hypot(Moving_track[-1][0]-center[0],Moving_track[-1][1]-center[1])
                Speed = (d_dist/0.04)*0.075
                #print('Delta_dist:', d_dist)
                #d_dist =round(d_dist,2)
                temp = "{:0>.2f}".format(Speed)
                cv2.putText(img,'Speed: '+temp,(50,50),font,1,(255,255,255),2,cv2.LINE_AA)
                cv2.putText(img,'cm/s',(280,50),font,1,(255,255,255),2,cv2.LINE_AA)

                Peak_speed = max(Peak_speed,Speed)
                temp2 = "{:0>.2f}".format(Peak_speed)
                cv2.putText(img,'Peak speed: '+temp2,(50,80),font,1,(255,255,255),2,cv2.LINE_AA)
                cv2.putText(img,'cm/s',(380,80),font,1,(255,255,255),2,cv2.LINE_AA)

                #cv2.rectangle(img,(center[0]-45,center[1]-45),(center[0]+45,center[1]+45),[255,255,255],2)
                #cv2.imshow('img_raw',img_raw)
                #img[1:91,-91:-1] = img_raw[center[1]-45:center[1]+45,center[0]-45:center[0]+45]

                Moving_track.append(center)


                points = np.array(Moving_track)
                cv2.polylines(img,np.int32([points[1:]]),0,(0,0,255))

                out.write(img)
                line = str(center[0])+','+str(center[1])+','+str(Speed)+'\n'
                with open('/users/zhangguangwei/desktop/Mouse_MS_track.csv','a') as f:
                    f.write(line)


        except ZeroDivisionError:
            print("error")

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
