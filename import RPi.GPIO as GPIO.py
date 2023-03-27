import RPi.GPIO as GPIO
from time import sleep, time
import sys
dac = [26,19,13,6,5,11,9,10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)

def perev(value,n):
    return [int(element) for element in bin(value)[2:].zfill(n)]
T = input()
while (True):
    if not T.isdigit():
        print('try again')
        print()
    t = int(T)/512
    for i in range(256):
        GPIO.output(dac,perev(i,8))
        sleep(t)
    for i in range (255, -1, -1):
        perev(i)
        GPIO.output(dac, perev(i,8))
        sleep(t)

GPIO.output(dac, 0)
GPIO.cleanup()
