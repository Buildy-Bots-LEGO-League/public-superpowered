from spike import MotorPair


def doSomething(motor_pair):
  motor_pair.move(10.0)




mp = MotorPair("A","B")

mp.set_default_speed(100)

doSomething(mp)
doSomething(mp)


mp.start_at_power(100, 0)
