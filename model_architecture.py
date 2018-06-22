from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Activation
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import LeakyReLU
from keras import backend as k
from keras import regularizers

class Model:
    def __init__(self,width,height,channels,num_classes):
        self.width=width
        self.height=height
        self.channels=channels
        self.num_classes=num_classes
    def model(self):
        model=Sequential()
        input_Shape=(self.height,self.width,self.channels)
        if(k.image_data_format=="channels_first"):
            input_Shape=(self.channels,self.height,self.width)
        model.add(Conv2D(20,(5,5),padding="same",input_shape=input_Shape))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
        model.add(Conv2D(50,(5,5),padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
        model.add(Flatten())
        model.add(Dense(500))
        model.add(Activation("relu"))
        model.add(Dense(self.num_classes))
        model.add(Activation("softmax"))
        return model


    def model2(self):
        model=Sequential()
        input_Shape=(self.height,self.width,self.channels)
        if(k.image_data_format=="channels_first"):
            input_Shape=(self.channels,self.height,self.width)
        model.add(Conv2D(20,(5,5),padding="same",input_shape=input_Shape))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
        model.add(Conv2D(50,(5,5),padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
        model.add(Conv2D(100,(5,5),padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
        model.add(Flatten())
        model.add(Dense(500))
        model.add(Activation("relu"))
        model.add(Dense(self.num_classes))
        model.add(Activation("softmax"))
        return model




    def model3(self):
        model=Sequential()
        input_Shape=(self.height,self.width,self.channels)
        if(k.image_data_format=="channels_first"):
            input_Shape=(self.channels,self.height,self.width)
        model.add(Conv2D(20,(5,5),padding="same",input_shape=input_Shape,kernel_regularizer=regularizers.l2(0.01)))
        model.add(LeakyReLU(alpha=0.1))
        model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
        model.add(Conv2D(50,(5,5),padding="same",kernel_regularizer=regularizers.l2(0.01)))
        model.add(LeakyReLU(alpha=0.1))
        model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
        model.add(Conv2D(100,(5,5),padding="same",kernel_regularizer=regularizers.l2(0.01)))
        model.add(LeakyReLU(alpha=0.1))
        model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
        model.add(Flatten())
        model.add(Dense(500))
        model.add(LeakyReLU(alpha=0.1))
        model.add(Dense(self.num_classes))
        model.add(Activation("softmax"))
        return model




        
    
    

        
