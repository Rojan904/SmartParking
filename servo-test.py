import RPi.GPIO as GPIO
import time

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

servoPIN = 18
GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 18 for PWM with 50Hz
p.start(2.5)  # Initialization



p.ChangeDutyCycle(2.5)
time.sleep(3)
p.ChangeDutyCycle(7.5)
time.sleep(3)
p.ChangeDutyCycle(2.5)



if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000)
