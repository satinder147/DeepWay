import cv2

class Stop:
    def __init__(self):
        self.cas=cv2.CascadeClassifier('stopsign_classifier.xml')
        
    def detect(self,frame):
        x=0
        y=0
        h=0
        w=0
        frame=cv2.resize(frame,(640,480))
        #cv2.imshow('fra',frame)
        frame2=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.imshow('fra',frame2)
        boxes=self.cas.detectMultiScale(frame2,1.3,5)
        for (x,y,w,h) in boxes:
            frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        if(x==0):
            return frame,-1
        elif((x+w)>320):
            #print((x+w)/2)
            return frame,0
        elif((x+w)<=320):
            #print((x+w)/2)
            return frame,1
        else:
            return frame,-1
        
        
