import RPi.GPIO as GPIO
import sys
import time
from threading import Thread

#sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522
import pigpio
GPIO.setwarnings(False)
# Initialization


class rfid(Thread):
    print("rfid init")
    def __init__(self, mysqlcon, callback):
        
        print(mysqlcon)
        self.servoPIN = 18
        GPIO.setmode(GPIO.BCM)
        self.callback = callback
        # GPIO.setup(servoPIN, GPIO.OUT)

        Thread.__init__(self)
        self.daemon = True
        self.conn = mysqlcon
        self.reader = SimpleMFRC522()

        #self.piGPIO = pigpio.pi()
        #self.piGPIO.set_PWM_frequency(self.servoPIN, 50)
        #self.piGPIO.set_PWM_dutycycle(self.servoPIN, (7.5/100)*255)
        #time.sleep(3)
        #self.piGPIO.set_PWM_dutycycle(self.servoPIN, (2.5/100)*255)
        
        self.start()

    def run(self):
        print("test")
        while True:
            print("Hold a tag near the reader")

            id, text = self.reader.read()
            print(f"id: {id} text: {text}")

            isGood = self.conn.get_data(f"SELECT * FROM SmartParking.RFID WHERE SmartParking.RFID.Address = '{str(id)}';")
            print(isGood)
            if isGood:
                print("open")
                self.callback()
                print("stopped")
            else:
                print("sorry")
                time.sleep(3)
