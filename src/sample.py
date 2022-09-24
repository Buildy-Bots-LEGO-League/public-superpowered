#imports
from spike import App
from spike import MotorPair
from spike import Motor
###############
#variables
app = App()#app
CD = MotorPair('C','D')#change for the specific robot's driving motors
Num = 0#counter
sped = 30#speed
#B = Motor('B')
###############
#program
for i in range(10):#loop 10 times
	app.start_sound("Coin", 100)#make a sound
	CD.move(-10, 'cm', 0, sped)#move back 10 centimeters at sped speed
	CD.move_tank(1.47, 'rotations', (-1*sped), sped)#turn 180 degrees at sped speed(1.47 rotations = 180 degrees for small wheel)
	Num+=1#counts on the computer
	print(Num)#shows abv
