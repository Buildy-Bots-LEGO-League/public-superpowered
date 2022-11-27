from spike import PrimeHub, MotorPair, Motor, ColorSensor, LightMatrix

motorPair = MotorPair("A", "B")

leftMotor = Motor("A")

primeHub = PrimeHub()

lightMatrix = primeHub.light_matrix

leftSensor = ColorSensor("C")
rightSensor = ColorSensor("D")

base_power = 40.0

def single_follow(distance):
    leftMotor.set_degrees_counted(0)

    goal_degrees = (distance / 17.5) * 360

    correction_factor = 0.3
    while leftMotor.get_degrees_counted() < goal_degrees:
        error = leftSensor.get_reflected_light() - 50
        correction = error * correction_factor
        motorPair.start_tank_at_power(int(base_power + correction), int(base_power - correction))
    motorPair.stop()

def find_line():
    motorPair.start(0, 40)
    while leftSensor.get_reflected_light() > 40:
        pass
    motorPair.stop()

		
def double_follow(duration):
    timer.reset()
    correction_factor = 0.2

    while timer.now() < duration:
        error = leftSensor.get_reflected_light() - rightSensor.get_reflected_light()
        correction = error * correction_factor
        motorPair.start_tank_at_power(int(basePower + correction), int(basePower - correction))
    motorPair.stop()

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

def drive(duration):
    primeHub.motion_sensor.reset_yaw_angle()
    correction_factor = 3
    while timer.now() < duration:
        error = primeHub.motion_sensor.get_yaw_angle()
        correction = error * correction_factor
        AB.start_tank_at_power(int(basePower - correction), int(basePower + correction))
    AB.stop()
