import dlib
import cv2

class detect:
    def __init__(self):
        self.detector=dlib.get_frontal_face_detector()
    def draw(self,frame,x,y,w,h):
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        return frame,(x+w)
        
    def faceDetect(self,frame):
        y=0
        
        frame=cv2.resize(frame,(480,640))
        grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        rect=self.detector(grey,1)
        for i,d in enumerate(rect):
            frame,y=self.draw(frame,d.left(),d.top(),d.right()-d.left(),d.bottom()-d.top())
        if(y==0):
            return frame,-1
        elif(y<150):
            return frame,1
        elif(y>=150):
            return frame,0
        
