#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()
brick.light(Color.RED)

motorR = Motor(Port.B)
motorL = Motor(Port.C)
ultraSense = UltrasonicSensor(Port.S3)

dist = 69
sped = 69

motorL.run(sped)
motorR.run(sped)

while dist < ultraSense.distance():
    brick.sound.beep(69)

motorR.stop(Stop.BRAKE)
motorL.stop(Stop.BRAKE)
