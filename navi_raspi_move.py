#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import pigpio

pi = pigpio.pi()
pi.set_mode(22, pigpio.OUTPUT) 
pi.set_mode(23, pigpio.OUTPUT) 
pi.set_mode(24, pigpio.OUTPUT) 
pi.set_mode(25, pigpio.OUTPUT) 
pi.set_PWM_frequency(22, 100)
pi.set_PWM_frequency(23, 100)
pi.set_PWM_frequency(24, 100)
pi.set_PWM_frequency(25, 100)

print('start')
pi.set_PWM_dutycycle(22, 0)
pi.set_PWM_dutycycle(23, 0)
pi.set_PWM_dutycycle(24, 0)
pi.set_PWM_dutycycle(25, 0)

duty_forward = 130
duty_direction =  160
rate_x = 10
rate_z = 5

def callback(msg):
    linear_x = round(msg.linear.x, 3)
    print(linear_x)
    if linear_x <0 :
        linear_x = linear_x * -1
    angular_z = round(msg.angular.z, 3)

    r_moter = int(duty_forward * linear_x * rate_x + duty_direction * angular_z * rate_z)
    l_moter = int(duty_forward * linear_x * rate_x - duty_direction * angular_z * rate_z)

    r_moter_23 = 0
    l_moter_25 = 0
    if r_moter > 0 :
        if r_moter > duty_direction :
            r_moter_22 = duty_direction
        else:
            r_moter_22 = r_moter
    else:
        r_moter_22 = 0
    
    if l_moter > 0 :
        if l_moter > duty_direction :
            l_moter_24 = duty_direction
        else:
            l_moter_24 = l_moter
    else:
        l_moter_24 = 0

    print(linear_x, angular_z)
    print(r_moter_22, l_moter_24)

    pi.set_PWM_dutycycle(22, r_moter_22)
    pi.set_PWM_dutycycle(23, r_moter_23)
    pi.set_PWM_dutycycle(24, l_moter_24)
    pi.set_PWM_dutycycle(25, l_moter_25)
        
if __name__ == '__main__':
    rospy.init_node('navi_raspi_move', anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, callback)
    rospy.spin()
