import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_19991 import robot_19991
#
def mission_one(r):
    print("Running Mission 1")
r.robot.settings(straight_speed=600, straight_acceleration=200)
r.robot.straight(590)
r.robot.settings(straight_speed=300, straight_acceleration=200)
r.robot.straight(140)
r.robot.settings(straight_speed=1000, straight_acceleration=200)
r.robot.straight(730)