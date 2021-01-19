#thu vien RPi.GPIO
import RPi.GPIO as IO
#thu vien Time
import time
#chan GPIO18 cho led
led = 18

#chon kieu BCM
IO.setmode(IO.BCM)
#Khai bao led la chan OUTPUT
IO.setup(led,IO.OUT)
#tat canh bao
IO.setwarnings(False)

try: 
        #Lap vo han
        while(True):
                #xuat high
                IO.output(led,1)
                #dung 1s
                time.sleep(1)
                #xuat LOW
                IO.output(led,0)
                time.sleep(1)
except KeyboardInterrupt:
        #lam sach chan
        IO.cleanup()
        print('OK')

