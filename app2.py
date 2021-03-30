import time
from RPi import GPIO
from flask import Flask, jsonify, request
from flask_socketio import SocketIO
from flask_cors import CORS
from DP1Database import Database

import rfidreader

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)
conn = Database(app=app, user='smartParking', password='parking',
                db='SmartParking', host='localhost', port=3306)


slagboom = rfidreader.rfid(conn)

# refers to the class that makes the lighting work
# licht = ldr.Verlichting(conn)

# parking = parkingSensor.parkingSensor(conn)


# if __name__ == '__main__':
#   socketio.run(app, host="0.0.0.0", port="5000")
