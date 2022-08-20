#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Joy
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

duty_forward = 150
duty_direction = duty_forward + 5
duty_max =255

def callback(joy_msg):
    global duty_forward, duty_direction, duty_max
    axes =[int(joy_msg.axes[0]),  int(joy_msg.axes[1])]
    buttonsA = int(joy_msg.buttons[0])
    buttonsB = int(joy_msg.buttons[1])
    print(axes, buttonsA, buttonsB, duty_forward, duty_direction)
    if axes == [0, 1]:
        print('forward')
        duty = duty_forward
        pi.set_PWM_dutycycle(22, duty)
        pi.set_PWM_dutycycle(23, 0)
        pi.set_PWM_dutycycle(24, duty)
        pi.set_PWM_dutycycle(25, 0)

    elif axes == [0, -1]:
        print('back')
        duty = duty_forward
        pi.set_PWM_dutycycle(22, 0)
        pi.set_PWM_dutycycle(23, duty)
        pi.set_PWM_dutycycle(24, 0)
        pi.set_PWM_dutycycle(25, duty)

    elif axes == [-1, 0]:
        print('right')
        duty = duty_direction
        pi.set_PWM_dutycycle(22, 0)
        pi.set_PWM_dutycycle(23, 0)
        pi.set_PWM_dutycycle(24, duty)
        pi.set_PWM_dutycycle(25, 0)

    elif axes == [1, 0]:
        print('left')
        duty = duty_direction
        pi.set_PWM_dutycycle(22, duty)
        pi.set_PWM_dutycycle(23, 0)
        pi.set_PWM_dutycycle(24, 0)
        pi.set_PWM_dutycycle(25, 0)

    elif buttonsA == 1:
        if duty_forward <= duty_max - 10:
            duty_forward = duty_forward + 10
            duty_direction = duty_forward + 5
        print('duty : ', duty_forward)
    elif buttonsB == 1:
        if duty_forward >= 5:
            duty_forward = duty_forward - 10
            duty_direction = duty_forward + 5
        print('duty : ', duty_forward)

    else:
        print('stop')
        pi.set_PWM_dutycycle(22, 0)
        pi.set_PWM_dutycycle(23, 0)
        pi.set_PWM_dutycycle(24, 0)
        pi.set_PWM_dutycycle(25, 0)

if __name__ == '__main__':
    rospy.init_node('joy_sub_raspi_move', anonymous=True)
    rospy.Subscriber("joy", Joy, callback)
    rospy.spin()
