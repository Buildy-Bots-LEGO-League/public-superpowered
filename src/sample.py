#imports
from spike import App
from spike import MotorPair
from spike import Motor
from spike import PrimeHub

###############
#functions
def turn(degrees=0, speed=100):
    real_degrees = degrees*.95
    hub.motion_sensor.reset_yaw_angle()
    yaw = hub.motion_sensor.get_yaw_angle()
    CD.start_tank(speed,speed*-1)
    while(abs(yaw)<real_degrees):
        yaw = hub.motion_sensor.get_yaw_angle()
    CD.stop()

def left(degrees=0, speed=100):
    turn(degrees,speed*-1)

def right(degrees=0, speed=100):
    turn(degrees,speed)
###############
#variables
app = App()#app
CD = MotorPair('C','D')#change for the specific robot's driving motors
Num = 0#counter
sped = 30#speed
hub = PrimeHub()#forMotionSensorForYaw
#B = Motor('B')
###############
#program
for i in range(10):#loop 10 times
    app.start_sound("Coin")#make a sound
    CD.move(10, 'cm', 0, sped)#move back 10 centimeters at sped speed
    left(180,30)
    Num+=1#counts on the computer
    print(Num)#shows abv

app.play_sound("Bonk")#finish indicator
