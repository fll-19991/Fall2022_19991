# Import the necessary libraries
import sys
import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

################################
# Define custom_robot Class
################################
class robot_19991:

    def __init__(self):
        '''
        this is the construtor for our robot class. 
        This function gets called when a robot object is made from the robot class.
        '''

        # Initialize the brick, motors, sensors
        # Use "try" so there can be an exception if there is an initialization error
        try:
            self.ev3 = EV3Brick()  
            self.ev3.light.on(Color.GREEN)
            self.ev3.speaker.beep(frequency=400, duration=200)
        except:
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"BRICK ERROR")
            self.ev3.print("BRICK ERROR")
            self.ev3.speaker.beep(frequency=2000, duration=2000)
            wait(2000)
            sys.exit()

        try:
            self.left_attachment_motor = Motor(Port.A)
        except:
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"PORT A MOTOR")
            print("PORT A MOTOR ERROR")
            self.ev3.speaker.beep(frequency=2000, duration=2000)
            wait(2000)
            sys.exit()
    
        try:
            self.left_drive_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
        except:
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"PORT B MOTOR")
            print("PORT B MOTOR ERROR")
            self.ev3.speaker.beep(frequency=2000, duration=2000)
            wait(2000)
            sys.exit()

        try:
            self.right_drive_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
        except:
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"PORT C MOTOR")
            print("PORT C MOTOR ERROR")
            self.ev3.speaker.beep(frequency=2000, duration=2000)
            wait(2000)
            sys.exit()

        try:    
            self.right_attachment_motor = Motor(Port.D)
        except:
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"PORT D MOTOR")
            print("PORT D MOTOR ERROR")
            self.ev3.speaker.beep(frequency=2000, duration=2000)
            wait(2000)
            sys.exit()

        try:
            self.robot = DriveBase(self.left_drive_motor, self.right_drive_motor, wheel_diameter=88, axle_track=111)
            self.robot.settings(straight_speed=600, straight_acceleration=200, turn_rate=200, turn_acceleration=100)
        except:
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"DRIVEBASE ERROR")
            print("DRIVEBASE ERROR")
            self.ev3.speaker.beep(frequency=2000, duration=2000)
            wait(2000)
            sys.exit()

        try: 
            self.left_color_sensor = ColorSensor(Port.S1)
        except:
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"PORT 1 SENSOR")
            print("PORT 1 SENSOR ERROR")
            self.ev3.speaker.beep(frequency=2000, duration=2000)
            wait(2000)
            sys.exit()

        try:
            self.right_color_sensor = ColorSensor(Port.S4)
        except:
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"PORT 4 SENSOR")
            print("PORT 4 SENSOR ERROR")
            self.ev3.speaker.beep(frequency=2000, duration=2000)
            wait(2000)
            sys.exit()

        self.ev3.screen.clear()
        self.ev3.light.off()
        self.ev3.light.on(Color.GREEN)
        self.ev3.screen.draw_text(10,40,"STARTUP GOOD!")
        wait(1000)
        self.ev3.screen.clear()    