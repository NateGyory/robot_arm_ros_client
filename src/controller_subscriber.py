#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy

from command import Command
from client import Client

class ControllerSubscriber:
    def __init__(self):
        self.client = Client()
        self.button_motor_map = {
            0: 'servo2',
            2: 'servo3',
            3: 'servo4',
            1: 'servo5'
        }

        rospy.init_node('controller_subscriber', anonymous=True)
        rospy.Subscriber("joy", Joy, self.callback, queue_size=1)
        rospy.spin()

    def send_data(self, axes, buttons):
        print(axes, buttons)
        command = None
        y_val = axes[1]
        x_val = axes[3]
        is_base = 1 if abs(x_val) > 0 else 0

        if is_base:
            # Right joytick
            direction = 1 if x_val > 0 else -1
            command = Command('servo1', x_val)
        else:
            # Left joystick
            direction = 1 if x_val > 0 else -1

            # Get idx of button which is pressed
            try:
                idx = buttons.index(1)
            except ValueError:
                return

            # If button is not suported return
            if idx not in self.button_motor_map:
                return

            motor = self.button_motor_map[idx]
            command = Command(motor, y_val)

        client.send_request(command)


    def callback(self, data):
        self.send_data(data.axes, data.buttons)

