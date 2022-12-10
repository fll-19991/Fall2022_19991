
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
    print("Running Mission 2 Ambitious Version")
    r.ev3.screen.draw_text(30, 60, "Mission 2")
    wait(1000)
    r.ev3.screen.clear()
    r.robot.stop()
    r.robot.settings(straight_speed=2000, straight_acceleration=250, turn_rate=100, turn_acceleration=100)
    #head out just a bit
    r.robot.straight(200)
    #turn to toy factory
    r.robot.turn(-60)
    #Go to toy factory
    r.robot.straight(590)
    #Dump in toy factory
    r.left_attachment_motor.run_angle(-60,-100)
    r.left_attachment_motor.stop
    #arm OUT OF MY WAY
    r.left_attachment_motor.run_angle(-35,100)
    r.left_attachment_motor.stop()
    #Back Up
    r.robot.straight(-220)
    #Turn towards the other mission
    r.robot.turn(-90)
    #Arm down
    r.left_attachment_motor.run_time(200,330)
    r.left_attachment_motor.hold()
    #To the other one
    r.robot.straight(840)
    #Up with the bar
    r.left_attachment_motor.stop()
    r.left_attachment_motor.run_angle(-45,-100)
    


    
   

   