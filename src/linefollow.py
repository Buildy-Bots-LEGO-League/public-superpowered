from spike import PrimeHub, MotorPair, ColorSensor
from spike.control import Timer


motorPair = MotorPair("A", "B")
primeHub = PrimeHub()

leftSensor = ColorSensor("C")
rightSensor = ColorSensor("D")

basePower = 40.0

timer = Timer()


def single_follow(duration):
    timer.reset()

    correction_factor = 0.3
    while timer.now() < duration:
        error = leftSensor.get_reflected_light() - 50
        correction = error * correction_factor
        motorPair.start_tank_at_power(int(basePower + correction), int(basePower - correction))
    motorPair.stop()


def double_follow(duration):
    correction_factor = 0.3

    while timer.now() < duration:
        error = leftSensor.get_reflected_light() - rightSensor.get_reflected_light()
        correction = error * correction_factor
        motorPair.start_tank_at_power(int(basePower + correction), int(basePower - correction))
    motorPair.stop()


while True:
    if primeHub.left_button.was_pressed():
        single_follow(15)
    if primeHub.right_button.was_pressed():
        double_follow(15)
