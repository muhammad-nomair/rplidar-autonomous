# rplidar-autonomous

this project required 
Rplidar
Raspberry Pi
Arduino board
Motor driver
Dc motors

install ubuntu mate 16.04 in raspberry pi.
install Ros Kinitic.

create workspace and clone this project in src.

upload car.ino in your arduino board.

run these cmds
  sudo chmod 666 /dev/ttyUSB0
  sudo chmod 666 /dev/ttyACM0
  roslaunch rplidar_ros rplidar.launch 
  
  after that run autonomous.py.
  
  
  autonomus.py will subscribe the data from rplidar/scan node and drive the motors.
