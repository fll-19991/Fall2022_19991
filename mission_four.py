import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_19991 import robot_19991

sensor_4 = ColorSensor(Port.S4)
## NO MY COMMENT
def mission_four(r):
    print("Running Mission 4")
    r.ev3.screen.draw_text(30, 60, "Mission 4")
    wait(1000)
    r.ev3.screen.clear()
    r.robot. straight(880)
    r.left_attachment_motor.run_angle(-200,50)
    r.left_attachment_motor.run_angle(-200,-50)
    r.left_attachment_motor.run_angle(-200,50)
    r.left_attachment_motor.run_angle(-200,-50)
    r.left_attachment_motor.run_angle(-200,50)
    r.left_attachment_motor.run_angle(-200,-50)
    r.robot. straight(-200)

  

  