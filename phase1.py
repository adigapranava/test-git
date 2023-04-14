import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

button_pin = 2
led_pin = 3
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin, False)

import pyrebase
import json

# Read the private key JSON file
with open("./private_key.json") as f:
    private_key = json.load(f)

config = {
  "apiKey": "AIzaSyAqxju-ukKbiwSAiAxVT6ZXwyzfGInAviY",
  "authDomain": "golden-gateway-346003.firebaseapp.com",
  "databaseURL": "https://golden-gateway-346003-default-rtdb.firebaseio.com",
  "projectId": "golden-gateway-346003",
  "messagingSenderId": "372919203020",
  "storageBucket": "golden-gateway-346003.appspot.com",
  "appId": "1:372919203020:web:c80ee5876ed4787ffdbe69",
  "measurementId": "G-YECVCGG9Y0"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

while True:
    # Read the button state
    button_state = GPIO.input(button_pin)
    
    # If the button is pressed
    if button_state == False:
        print("pressed")
        # Turn on the LED
        GPIO.output(led_pin, True)
        db.child("door").set({"state":True})
        time.sleep(0.2)
    else:
        # Turn off the LED
        print("not pressed")
        db.child("door").set({"state":False})
        GPIO.output(led_pin, False)
