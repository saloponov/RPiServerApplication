from gpiozero import Button, LED
from time import sleep

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")
from time import sleep


"""for i in range(30):
    print(i)
    led = LED(i)
    led.on()
"""
while True:
    value = input()
    value = int(value)
    if value == "q":
        break
    GPIO.cleanup(value)
    GPIO.setup(value, GPIO.OUT)
    
    GPIO.output(value, GPIO.HIGH)
    print(value)
    sleep(2)
    GPIO.output(value, GPIO.LOW)
    sleep(1)
    GPIO.cleanup(value) 
    
    
    
    
