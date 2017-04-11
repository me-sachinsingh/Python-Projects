import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(3, gpio.OUT)
gpio.setup(7, gpio.IN)

pir_state = 0

try:
    while True:
        while pir_state is 0:
            pir_state = gpio.input(7)
            gpio.output(3, gpio.LOW)
            
        print("state = %r" %pir_state)
        if pir_state == 1:
            gpio.output(3, gpio.HIGH)
        else:
            gpio.output(3, gpio.LOW)
        pir_state = 0

except KeyboardInterrupt:
    gpio.cleanup()

