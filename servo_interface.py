# interfacing func for servo control

import RPi.GPIO as GPIO
#import time
import numpy

class servo_controller:
    def __init__(self)
        # initialise servo to center position
        GPIO.setmode(GPIO.BOARD)
        x_pin = 12
        #y_pin = 35

        GPIO.setup(x_pin, GPIO.OUT)
        x_out = GPIO.PWM(x_pin, 50)
        #GPIO.setup(y_pin, GPIO.OUT)
        #y_out = GPIO.PWM(y_pin, 50)

        cen_pos = 7.5
        clockwise_pos = 12.5
        anticlockwise_pos = 2.5
        # start at 90 degree
        x_out.start(7.5)
        #y_out.start(7.5)
        # coordinates of screen center
        center = (0, 0)
        x_screen = 720
        #y_screen = 480
        focal_len = 3.04
        x_ccd = 3.68
        #y_ccd = 2.76

    def servo_move(target):
        # move the camera towards screen center
        x_diff = target(0) - center(0)
        #y_diff = target(1) - center(1)
        x_degree = numpy.arctan(x_ccd*2*x_diff/x_screen/focal_len) + numpy.pi/2
        #y_degree = numpy.arctan(y_ccd*2*y_diff/y_screen/focal_len) + numpy.pi/2
        x_dc = x_degree/numpy.pi*(clockwise_pos - anticlockwise_pos) + anticlockwise_pos
        #y_dc = y_degree/numpy.pi*(clockwise_pos - anticlockwise_pos) + anticlockwise_pos
        x_out.ChangeDutyCycle(x_dc)
        #y_out.ChangeDutyCycle(y_dc)

    def servo_stop(self):
        # clean up
        x_out.stop()
        #y_out.stop()
        GPIO.cleanup()

