import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
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
    r.robot.straight(720)
    r.left_attachment_motor.run_angle(-200,50)
    r.left_attachment_motor.run_angle(-200,-50)
    r.left_attachment_motor.run_angle(-200,50)
    r.left_attachment_motor.run_angle(-200,-50)
    r.left_attachment_motor.run_angle(-200,50)
    r.left_attachment_motor.run_angle(-200,-50)
    r.left_attachment_motor.stop()
    #r.robot.straight(-1)
    #wait(500)
    #r.robot.stop()
    # wait(500)
    #r.robot.settings(straight_speed=600, straight_acceleration=200, turn_rate=200, turn_acceleration=100)
    r.robot.turn(-180)
    r.robot.straight(-445)
    #r.robot.straight(-100)
    #r.robot.turn(-100)
    #r.left_attachment_motor.run_angle(200,185)
    #r.robot.turn(50)
    r.robot.turn(65) 
    r.robot.straight(-350)
    r.robot.turn(-80)
    r.robot.straight(-540)
    #r.robot.straight(350)
    robot.straight(400)
    robot.turn(40)
    robot.straight(800)