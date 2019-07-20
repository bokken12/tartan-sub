#!/usr/bin/env python
import rospy


from mover import Mover
from gate import Gate
from visual_servo import DarknetVisualServo
from config import Config
from armer import Armer


class ControlSub(object):
    def __init__(self):
        self.mover = Mover()
        self.armer = Armer()


if __name__ == "__main__":
    rospy.init_node('main', anonymous=True)

    gate = Gate()
    dice = DarknetVisualServo(Config.darknet_topic, Config.zed_camera_dims, 'D6')

    print("Arming")
    armer.arm()

    print("Gate")
    gate.run()

    print("Turning")
    mover.turn(Config.dice_yaw_time, Config.dice_yaw_speed)

    print("Dice")
    vamp.run()