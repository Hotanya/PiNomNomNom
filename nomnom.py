import RPi.GPIO as GPIO
import time

channel = 17
#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel);
        print("hello world") #do something
    
    else:
        pass #do nothing

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) #is pin HIGH or LOW
GPIO.add_event_callback(channel, callback) #assign function to GPIO pin

