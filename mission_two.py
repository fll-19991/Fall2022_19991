import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_19991 import robot_19991

def mission_two(r):
    print("Running Mission 2")
    r.ev3.screen.draw_text(30, 60, "Mission 2")
    wait(1000)
    r.ev3.screen.clear()

    r.robot.settings(straight_speed=1000, straight_acceleration=100, turn_rate=100, turn_acceleration=100)
   
    r.robot.straight(150)
    r.robot.turn(-70)
    r.robot.straight(800)
    r.left_attachment_motor.run_angle(400,40)
    r.left_attachment_motor.stop
    r.robot.straight(-200)
