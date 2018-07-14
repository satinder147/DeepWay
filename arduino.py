import serial

class Arduino:
    def __init__(self,baudrate,COM,timeout=1):
        self.timeout=timeout
        self.COM=COM
        self.baudrate=baudrate
        self.a=serial.Serial(self.COM,self.baudrate,timeout=self.timeout)
    
    def movleft(self):
        self.a.write(b'1')
        data=self.a.readline().decode('ascii')
        print(data)
    def movright(self):
        self.a.write(b'2')
        data=self.a.readline().decode('ascii')
        print(data)
        
        
