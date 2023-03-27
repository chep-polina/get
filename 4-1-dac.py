import RPi.GPI0 as GPIO
import sys
dac = [26, 19, 13, 6, 5, 11, 9, 10 ]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def perevod(a):
    return [int (elem) for elem in bin(a) [2:].zfill((n))]
    
try:
    while (True):
        a = int((input))
        if a == 'q':
            sys.exit()
        elif a.isdigit()  and int(a)%1 == 0 and 0 <= int((a)) <=255:
            GPIO.output(dac,perevod(int(a),8))
            print("{:.4f}".format(int(a)/256*3.3)) 
        elif not a.isdigit():
            print('введите число')

finally:
    GPIO.output(dac,0)
    GPIO.cleanup()