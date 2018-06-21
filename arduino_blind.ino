#include<Servo.h>
Servo x,y;
int a;
void setup()
{
  x.attach(2);
  y.attach(3);
  Serial.begin(9600);
  }
void loop()
{
  if(Serial.available()>0)
  {
    a=Serial.read();
    if(a=='1')
    moveLeft();
    if(a=='2')
    moveRight();
    }
  }

void moveLeft()
{
  x.write(135);
delay(500);
x.write(90);
delay(500);
  }

void moveRight()
{
y.write(54);
delay(500);
y.write(90);
delay(500);
  }
