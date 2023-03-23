#include <Servo.h>

int up = 165;
int down = 15;

Servo myservo1;  // create servo object to control a servo
Servo myservo2; 
// twelve servo objects can be created on most boards

int pos = down;    // variable to store the servo position

void setup() {
  myservo1.attach(2);  // attaches the servo on pin 9 to the servo object
  myservo2.attach(3);
}

void loop() {
  for (pos = down; pos <= up; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo1.write(pos);
    myservo2.write(pos);
    delay(5);                       // waits 15ms for the servo to reach the position
  }
  for (pos = up; pos >= down; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo1.write(pos);
    myservo2.write(pos);
    delay(5);                        // waits 15ms for the servo to reach the position
  }
//  myservo.write(90);
}
