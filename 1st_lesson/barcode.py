#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.light(Color.RED)
brick.sound.beeps(2)

ultraSense = UltrasonicSensor(Port.S3)

while True: 
    while ultraSense.distance() < 4000:
        wait(0.1)
        print('y')
    wait(2)
    brick.light(Color.GREEN)
    brick.sound.beep()
