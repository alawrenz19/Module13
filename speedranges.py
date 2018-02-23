import RoboPiLib as RPL
from setup import RPL
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)

print "Please type in the speed of your motors:"
NumberR = int(raw_input("Left Motor > "))
NumberL = int(raw_input("Right Motor > "))


RPL.servoWrite(1, NumberR)
RPL.servoWrite(7, NumberL)
