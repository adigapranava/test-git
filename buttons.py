import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

button_pin = 2
led_pin = 3
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin, False)

while True:
    # Read the button state
    button_state = GPIO.input(button_pin)
    
    # If the button is pressed
    if button_state == False:
        print("pressed")
        # Turn on the LED
        GPIO.output(led_pin, True)
        time.sleep(0.2)
    else:
        # Turn off the LED
        print("not pressed")
        GPIO.output(led_pin, False)
