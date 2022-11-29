from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
AB = MotorPair('A','B')
F = Motor('F')

for i in range(4):
    F.run_for_degrees(180)
    wait_for_seconds(1)
    F.run_for_degrees(-180)
    wait_for_seconds(1)
