import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_19991 import robot_19991
###
def mission_three(r):
    print("Running Mission 3")
    r.ev3.screen.draw_text(30, 60, "Mission 3")
    wait(1000)
    r.ev3.screen.clear()
    r.robot.straight(900)
    r.robot.turn(-90)
    r.robot.straight(900)
    r.robot.turn(90)
    r.robot.straight(40)
    r.left_attachment_motor.run_angle(-200,100) 