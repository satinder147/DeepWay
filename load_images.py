import cv2
import os
from keras.preprocessing.image import img_to_array


class load:
    def __init__(self, width, height, channels, paths):
        self.width = width
        self.height = height
        self.channels = channels
        self.paths = paths
        self.data = []
        self.labels = []

    def imgload(self):
        i = -1
        for folder in self.paths:
            i = i+1
            
            path = str(folder[0])
            folder = os.listdir(path)
            
            for file in folder:
                # print(file+" "+str(i))
                img = cv2.imread(path+'/'+file, -1)
                
                img = cv2.resize(img, (self.width, self.height))
                img = img_to_array(img)
                self.data.append(img)
                self.labels.append(i)
                
        return self.data, self.labels
