from spike import PrimeHub, MotorPair, ColorSensor, Motor
from spike.control import Timer


AB = MotorPair("A", "B")
primeHub = PrimeHub()
#mE = Motor("E")

leftSensor = ColorSensor("C")
rightSensor = ColorSensor("D")

basePower = 30.0

timer = Timer()

def turn(degrees=0, speed=100):
    real_degrees = degrees*.95
    primeHub.motion_sensor.reset_yaw_angle()
    yaw = primeHub.motion_sensor.get_yaw_angle()
    AB.start_tank(speed,speed*-1)
    while(abs(yaw)<real_degrees):
        yaw = primeHub.motion_sensor.get_yaw_angle()
    AB.stop()

def left(degrees=0, speed=100):
    turn(degrees,speed*-1)

def right(degrees=0, speed=100):
    turn(degrees,speed)

def single_follow(duration, correction_factor):
    timer.reset()

    while timer.now() < duration:
        error = leftSensor.get_reflected_light() - 50
        correction = error * correction_factor
        AB.start_tank_at_power(int(basePower + correction), int(basePower - correction))
    AB.stop()

def double_follow(duration):
    correction_factor = 0.3

    while timer.now() < duration:
        error = leftSensor.get_reflected_light() - rightSensor.get_reflected_light()
        correction = error * correction_factor
        AB.start_tank_at_power(int(basePower + correction), int(basePower - correction))
    AB.stop()


while(True):
    rightR = rightSensor.get_reflected_light()
    if(rightR>70):
        #if primeHub.left_button.was_pressed():
        single_follow(0.1,0.1)
        #if primeHub.left_button.was_pressed():
            #double_follow(15)
    else:
        print(rightR)
        AB.stop
