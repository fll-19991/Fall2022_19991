import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_19991 import robot_19991
##
def mission_five(r):
    print("Running Mission 5")
    r.ev3.screen.draw_text(30, 60, "Mission 5")
    wait(1000)
    #  r.ev3.screen.clear()
    # r.robot.straight(10)
    # r.robot.turn(15)  
    # r.robot.straight(190)
    # r.robot.turn(15)
    # r.robot.straight(300)
    #r.ev3.screen.clear()
    r.robot. straight(685)
    r.left_attachment_motor.run_angle(-200,50)
    r.left_attachment_motor.run_angle(-200,-50)
    r.left_attachment_motor.run_angle(-200,50)
    r.left_attachment_motor.run_angle(-200,-50)
    r.left_attachment_motor.run_angle(-200,50)
    r.left_attachment_motor.run_angle(-200,-50)
    #r.robot. straight(150)
    r.robot.turn(-185)
    r.robot.straight(-445)
    #r.robot.straight(-100)
    #r.robot.turn(-100)
    #r.left_attachment_motor.run_angle(200,185)
    r.robot.straight(-50)
    #r.robot.turn(50)
    r.robot.turn(65) 
    r.robot.straight(-350)
    r.robot.turn(115)
    r.robot.straight(-540)
    #r.robot.straight(350)