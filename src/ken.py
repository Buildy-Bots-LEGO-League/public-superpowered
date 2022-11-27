from spike import MotorPair, Motor, LightMatrix
from spike.control import sleep


def doSomething(motor_pair):
  motor_pair.move(10.0)




left_motor = Motor("E")

left_motor.set_default_speed(25)
left_motor.run_for_degrees()
sleep
mp = MotorPair("A","B")

mp.set_default_speed(100)

doSomething(mp)
doSomething(mp)


mp.start_at_power(100, 0)
