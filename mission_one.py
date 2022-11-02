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
    r.robot.straight(650)
    r.robot.straight(-280)
    #Start of new mission
    r.robot.stop()
    r.robot.settings(straight_speed=1000, straight_acceleration=1100, turn_rate=100, turn_acceleration=100)
    r.robot.turn(-40)
    r.robot.straight(855)
    r.robot.turn(95)
    r.robot.straight(300)
    wait(250)
    r.robot.straight(-255)
    r.robot.straight(300)
    wait(250)
    r.robot.straight(-255)
    r.robot.straight(300)
    wait(250)
    r.robot.straight(-255) 
    #r.robot.straight(300)
    #wait(1000)
    #r.robot.straight(-255)
    r.robot.turn(-90)
    r.robot.straight(-1070)
    #End of Code
    #VICTORY!!!!!
   
