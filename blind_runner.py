

from face_detection import detect
from arduino import Arduino
from voice import Voice
import time
import cv2
import numpy as np
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import datetime
from stop import Stop
model_name='blind_with_regularization.model'
COM='COM9'
camera=1
baudrate=9600
width=64
height=64
prob=0
label=''









print("loading model .....")
model=load_model(model_name)
print("model loaded")
ard=Arduino(baudrate,COM)##movleft(),movright()
vce=Voice()#left(),right()
st=Stop()
fac=detect()
current=datetime.datetime.now()
flag=None
cap=cv2.VideoCapture(camera)
ret=True
prev=None
while ret:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    
    faces=fac.faceDetect(frame)

    ##stop on left
    
      ##  you have a stop on '''
    current=datetime.datetime.now()
    new=current.second
    if((current.second)%4==0):
        if(prev!=new):
            sto,direction=st.detect(frame)
            if(direction==0):
                vce.stop_right()

            elif(direction==1):
                vce.stop_left()
                
            cv2.imshow('stop',sto)
            faces,dire=fac.faceDetect(frame)
            if(dire==0):
                vce.peopleOnRight()
            if(dire==1):
                vce.peopleOnLeft()
            cv2.imshow('faces',faces)            
            frame2=frame
            frame2=cv2.resize(frame2,(width,height))
            frame2=frame2.astype('float')/255.0
            frame2=img_to_array(frame2)
            frame2=np.expand_dims(frame2,axis=0)
            left,right,center=model.predict(frame2)[0]
            if(left>right and left >center):
                label='left'
                prob=left*100

            if(left<right and right >center):
                label='right'
                prob=left*right
                #vce.left()
                for i in range(1):
                    ard.movleft()
        
            if(center>right and left <center):
                label='center'
                prob=center*100
                #vce.left()
                for i in range(1):
                    ard.movleft()
            prev=new    
    cv2.putText(frame,label+" with probability "+str(prob),(10,25),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)
            
    
        
    cv2.imshow('frame',frame)
    

    

    if(cv2.waitKey(1)&0XFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()




