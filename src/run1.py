from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
AB = MotorPair('A','B')
E = Motor('E')#top
F = Motor('F')#side
leftSensor = ColorSensor('C')
rightSensor = ColorSensor('D')
rightMotor = Motor('B')
timer = Timer()


def driveDistance(distance,heading):
    print("ehrsfnikserhdsfijsdk")

    cm_per_degree = (17.5 / 360) * 0.1  
    turnToHeading(heading)
    '''base_power = 30
    rightMotor.set_degrees_counted(0)
    correction_factor = 3
    traveled = 0
    while traveled < distance:
        print('traveled',traveled)
        error = hub.motion_sensor.get_yaw_angle()
        correction = error * correction_factor
        AB.start_tank_at_power(int(base_power - correction), int(base_power + correction))
        traveled = cm_per_degree * rightMotor.get_degrees_counted()
        print("Traveled: %s" % traveled)
    AB.stop()'''


def turnToHeading(heading=0,speed=100):

    acceptableError = 3
    stopErrorSetting = 5.0
    
    allowedError = stopErrorSetting * (speed / 100.0)

    keepTurning = True#boolean
    while(keepTurning):
        # Should we turn left or right
        turnFactor = int(speed * leftOrRight(heading))
        print('turnFactor',turnFactor)
        AB.start_tank(turnFactor, turnFactor*-1)
        keepTurning = not (heading - allowedError <= getHeading() <= heading + allowedError)
    AB.stop()

    '''if (abs(getHeading() - heading) > acceptableError):
        print ("Outside allowed: %s, %s, %s" % (getHeading(), heading, acceptableError))
        turnToHeading(heading, speed/2)
    else:
        print("Inside allowed: %s, %s, %s" % (getHeading(), heading, acceptableError))
        '''
def leftOrRight(goal):
    current = getHeading()
    if current < goal:
        if goal - current < 180:
            return 1    # right
        else:
            return -1   # left
    else:
        if current - goal < 180:
            return -1   # left
        else:
            return 1    # right

def getHeading():
    heading = hub.motion_sensor.get_yaw_angle()
    if(heading<0):
        heading+=360
    return(heading)

driveDistance(5,10)

#exit(0)
