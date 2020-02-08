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

motorR = Motor(Port.B)
motorL = Motor(Port.C)
ultraSense = UltrasonicSensor(Port.S1)

dist = 500
sped = 666

while dist < ultraSense.distance():
    motorL.run(sped)
    motorR.run(sped)

motorR.stop()
motorL.stop()