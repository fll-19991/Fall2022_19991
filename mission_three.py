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
    #r.left_attachment_motor.run_angle(-800,-100)
    r.robot.stop()
    #r.robot.settings(straight_speed=2000, straight_acceleration=250, turn_rate=100, turn_acceleration=100)
    r.robot.straight(900)
    r.robot.turn(-90)
    r.robot.stop()
    r.robot.straight(900)
    r.robot.turn(87)
    r.robot.stop()
    r.robot.straight(70)
    r.left_attachment_motor.run_angle(-250,100)
    r.robot.stop() 
    r.robot.straight(-50)
    r.robot.turn(-300)
    r.robot.stop()
    r.robot.straight(1700)