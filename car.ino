#include <string.h>
#include <AFMotor.h>


// declare motors
AF_DCMotor motor1(1);
AF_DCMotor motor3(3);

void setup() {
    Serial.begin(115200);

}


// function to control motor
// speed is how fast the motor rotates



void control_motor1(int speed){

    if(speed > 0){
  motor1.run(FORWARD);
  motor1.setSpeed(speed);
    }
    else if(speed < 0){
  motor1.run(BACKWARD);
  motor1.setSpeed(-speed);
    }
    else{
  motor1.run(RELEASE);
    }
}


void control_motor3(int speed){

    if(speed > 0){
  motor3.run(FORWARD);
  motor3.setSpeed(speed);
    }
    else if(speed < 0){
  motor3.run(BACKWARD);
  motor3.setSpeed(-speed);
    }
    else{
  motor3.run(RELEASE);
    }
}



// In time loop, receive from serial and control 2 motors
void loop() {
    static int speed[6];
    static char buff[30];
    int counter = 0;

    // read command from raspberry pi
    while(Serial.available()){
        buff[counter] = Serial.read();
        if (counter > 30 || buff[counter] == '*') {
            buff[counter] = '\0';
            speed[0]=atoi(strtok(buff,","));
            speed[1]=atoi(strtok(NULL,","));
            speed[2]=atoi(strtok(NULL,","));
            speed[3]=atoi(strtok(NULL,","));
            speed[4]=atoi(strtok(NULL,","));
            speed[5]=atoi(strtok(NULL,","));
        }
        else{
            counter++;
        }
    }

    // control motors
    control_motor1(speed[0]);
    control_motor3(speed[1]);


    // send messages to raspberry pi
    Serial.print(speed[0]); Serial.print(",");
    Serial.print(speed[1]); Serial.print(",");
    
    Serial.print(speed[2]); Serial.print(",");
    Serial.print(speed[3]); Serial.print(",");
    Serial.print(speed[4]); Serial.print(",");
    Serial.println(speed[5]);

    delay(100);
}
