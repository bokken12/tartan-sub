#!/usr/bin/env python
import rospy

from motion_utilities import Mover
from gate import Gate
from vamp_visual_servo import VampVisualServoing
from config import ConfigMap, SimConfig, SubConfig
from armer import Armer


class SubController(object):
    def __init__(self, run_config):
        self.mover = Mover(run_config)
        self.armer = Armer(run_config)


if __name__ == "__main__":
    rospy.init_node('tartan_19_controller', anonymous=True)

    run_config = ConfigMap['Sim']
    sub_controller = SubController(run_config)

    print("Arming")
    sub_controller.armer.arm()

    print("Gate")
    # gate = Gate(sub_controller, run_config)
    # gate.execute("fancy")

    sub_controller.mover.dive(1, -0.4)

    print("Vamp")
    vamp = VampVisualServoing(sub_controller, run_config)
    vamp.execute()


    sub_controller.armer.disarm()

if __name__ == '__main__':
    main(sys.argv)
