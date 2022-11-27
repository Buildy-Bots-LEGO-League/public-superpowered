from spike import PrimeHub, MotorPair, Motor, ColorSensor, LightMatrix, Timer

timer = Timer()

motorPair = MotorPair("A", "B")

leftMotor = Motor("A")
rightMotor = Motor("B")

primeHub = PrimeHub()

lightMatrix = primeHub.light_matrix

leftSensor = ColorSensor("C")
rightSensor = ColorSensor("D")

base_power = 30.0

def single_follow(distance):
	rightMotor.set_degrees_counted(0)

	goal_degrees = (distance / 17.5) * 360

	correction_factor = 0.3
	while rightMotor.get_degrees_counted() < goal_degrees:
		error = leftSensor.get_reflected_light() - 50
		correction = error * correction_factor
		motorPair.start_tank_at_power(int(base_power + correction), int(base_power - correction))
		print("goal: %s " % (goal_degrees))
		print(rightMotor.get_degrees_counted())
	motorPair.stop()

def find_line():
	motorPair.start(0, 25)
	while leftSensor.get_reflected_light() > 40:
		pass
	motorPair.stop()

def turn(degrees=0, speed=100):
	real_degrees = degrees*.95
	primeHub.motion_sensor.reset_yaw_angle()
	yaw = primeHub.motion_sensor.get_yaw_angle()
	motorPair.start_tank(speed,speed*-1)
	while abs(yaw) < real_degrees:
		yaw = primeHub.motion_sensor.get_yaw_angle()
	motorPair.stop()

def left(degrees=0, speed=100):
	lightMatrix.show_image("ARROW_W")
	turn(degrees,speed*-1)
	lightMatrix.off()

def right(degrees=0, speed=100):
	lightMatrix.show_image("ARROW_E")
	turn(degrees,speed)
	lightMatrix.off()

def drive(distance):

	cm_per_degree = (17.5 / 360) * 1.0

	primeHub.motion_sensor.reset_yaw_angle()
	rightMotor.set_degrees_counted(0)
	correction_factor = 3
	traveled = 0
	lightMatrix.show_image("ARROW_N")
	while traveled < distance:
		error = primeHub.motion_sensor.get_yaw_angle()
		correction = error * correction_factor
		motorPair.start_tank_at_power(int(base_power - correction), int(base_power + correction))
		traveled = cm_per_degree * rightMotor.get_degrees_counted()
		print("Traveled: %s" % traveled)
	motorPair.stop()
	lightMatrix.off()