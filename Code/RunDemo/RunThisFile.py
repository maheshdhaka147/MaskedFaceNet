# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 07:59:02 2020

@author: mahes
"""

import numpy as np
import cv2
from mtcnn import MTCNN
detector=MTCNN()

from tensorflow.keras.models import load_model
model=load_model("model")
cap = cv2.VideoCapture(0)
#cap.set(3,1280)
#cap.set(4,720)
while(True):


    
    ret, frame = cap.read()
    
    
        
    try:
        myface=[]
        myface.append(detector.detect_faces(frame))
        total_face_found=len(myface[0])
        if total_face_found>=1:
            for i in range(0,total_face_found):
                myface=np.asarray(myface)
                x,y,width,height=myface[0][i]['box']
                updated_frame=frame[y:y+height,x:x+width:]
                arrayed_frame = np.dot(updated_frame[...,:3], [0.299, 0.587, 0.144])
                #gray_frame = cv2.cvtColor(updated_frame, cv2.COLOR_BGR2GRAY)
                resized_frame = cv2.resize(arrayed_frame, (16,16))
                #print(arrayed_frame)
                #cv2.imshow("",arrayed_frame.astype(int))
                reshaped_frame=np.reshape(resized_frame,(1,16,16,1))
                reshaped_frame=reshaped_frame/255
                outcome=model.predict_classes(reshaped_frame)
                print(outcome)
                if outcome==1:
                    cv2.rectangle(frame,(x,y),(x+width,y+height),(0,0,255),2)
                    cv2.imshow('Live Video',frame)
                elif outcome==0:
                    cv2.rectangle(frame,(x,y),(x+width,y+height),(0,255,0),2)
                    cv2.imshow('Live Video',frame)
        else:
          cv2.imshow('Live Video',frame)  

    except Exception as err:
        print(err)
        cv2.imshow('Live Video',frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

