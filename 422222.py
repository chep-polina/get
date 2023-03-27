import RPi.GPIO as GPIO
from time import sleep, time
import sys

GPIO.setwarnings(False)

def ppp(x):
    return [int(el) for el in bin(x)[2:].zfill(8)]

dac = [26,19,13,6,5,11,9,10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
try:
    count=0
    c=0
    while count!=500:
        if count<50 and c==0:
            count+=1
            a=ppp(count)
            GPIO.output(dac, a)
            sleep(0.05)
        else:
            c=1
            count-=1    
            a=ppp(count)
            GPIO.output(dac, a)
            sleep(0.05)
            if count==1:
                c==1
except:
    print('Одна ошибка и ты ошибся') 
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()