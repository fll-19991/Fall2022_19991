import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_19991 import robot_19991

def mission_one(r):
    print("Running Mission 1")
    r.ev3.screen.draw_text(30, 60, "Mission 1")
    wait(1000)
    r.ev3.screen.clear()
    r.robot.settings(straight_speed=1000, straight_acceleration=100, turn_rate=100, turn_acceleration=100)
    r.robot.straight(-920)
    #r.robot.settings(straight_speed=300, straight_acceleration=100, turn_rate=100, turn_acceleration=100)
    #r.robot.straight(-310)
    #r.robot.settings(straight_speed=1000, straight_acceleration=100, turn_rate=100, turn_acceleration=100)
    r.robot.straight(730)