#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import serial
from sensor_msgs.msg import LaserScan
import time


class driver:
    def __init__(self):
        # init ros
        rospy.init_node('car_driver_1')
        #rospy.Subscriber('/cmd_vel', Twist, self.get_cmd_vel)
        rospy.Subscriber('/scan', LaserScan,self.get_cmd_vel)
        self.ser = serial.Serial('/dev/ttyUSB1', 115200)
        self.get_arduino_message()

    # get cmd_vel message, and get linear velocity and angular velocity
    def get_cmd_vel(self, msg):
        front=msg.ranges[0]
        ft_lf=msg.ranges[45]
        left1=msg.ranges[90]
        ft_ri=msg.ranges[315]
        right1=msg.ranges[270]
        print('front = ' ,front)
        print('front_left = ' ,ft_lf)
        print('left  = ' ,left1)
        print('front_right' ,ft_ri)
        print('right = ' ,right1)

        base_speed =180
        turn_speed=205


        if front > 1:
            right =base_speed
            left = base_speed
            if left1 < .35:
                left =0
                right = base_speed
            elif right1 < .35:
                left =turn_speed
                right = 0


                  
        
        elif front < 1:
            right =0
            left = 0
            time.sleep(.01)
            if left1 > .5:
                left =turn_speed
                right =-turn_speed
            elif right1 > .5:
                left =-turn_speed
                right = turn_speed
            elif ft_lf <.5:
                right =turn_speed
                left = base_speed
            elif ft_ri<.5:
                right =turn_speed
                left = base_speed 
        
        elif front == inf:
                right = -base_speed
                left = -base_speed

            

            
        else:
            right = 0
            left = 0
            
        self.send_cmd_to_arduino(right, left)

    # translate x, and angular velocity to PWM signal of each wheels, and send to arduino
    def send_cmd_to_arduino(self, right1, left1):
        # calculate right and left wheels' signal


        right = int(right1) 
        left = int(left1)


        # format for arduino
        message = "{},{}*".format(right, left)
        print message
        # send by serial 
        self.ser.write(message)

    # receive serial text from arduino and publish it to '/arduino' message
    def get_arduino_message(self):
        pub = rospy.Publisher('arduino', String, queue_size=10)
        r = rospy.Rate(50)
        while not rospy.is_shutdown():
        
            message = self.ser.readline()
            pub.publish(message)
            r.sleep()
        

if __name__ == '__main__':
    try:
        d = driver()
    except rospy.ROSInterruptException: 
        pass