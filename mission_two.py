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
    r.robot.settings(straight_speed=2000, straight_acceleration=250, turn_rate=100, turn_acceleration=100)
   #oLD SPEED 1000, 100, 100, 100
   #head out just a bit
    r.robot.straight(200)
    #turn to toy factory
    r.robot.turn(-65)
    #Go to toy factory
    r.robot.straight(600)
    #Dump in toy factory
    r.left_attachment_motor.run_angle(-70,-100)
    r.left_attachment_motor.stop
    #arm OUT OF MY WAY
    r.left_attachment_motor.run_angle(-35,100)
    #Back Up
    r.robot.straight(-200)
    #to the next one
    r.robot.turn(-60)
    #to the other home 
    r.robot.straight(2600)
    r.ev3.speaker.beep(frequency=2000, duration=1000)
#YAY WE FINISHED!!!!!!!
#MISSION 2 DA BEST
#BETTER THAN YOURS Lillllllllllly
#HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA
#LOVE Me
