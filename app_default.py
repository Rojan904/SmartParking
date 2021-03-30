import time
from RPi import GPIO
from flask import Flask, jsonify, request,render_template
from flask_socketio import SocketIO, send,emit
from flask_cors import CORS
from DP1Database import Database
import ldr

#from LCD import LCD_run
import parkingSensor
import rfidreader
import pigpio

app = Flask(__name__,template_folder='template',static_folder='static')

CORS(app)
print("cors")
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)

conn = Database(app=app, user='smartParking', password='parking',
                db='SmartParking', host='localhost', port=3306)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/access.html")
def access():
    return render_template('access.html')

@app.route("/parking.html")
def parking():
    return render_template('parking.html')
# refers to the class that makes lcd run
# LCD_run()

# refers to the class that makes the lighting work
licht = ldr.Verlichting(conn)

servoPIN = 18
GPIO.setmode(GPIO.BCM)
piGPIO = pigpio.pi()
piGPIO.set_PWM_frequency(servoPIN, 50)
piGPIO.set_PWM_dutycycle(servoPIN, (2.5 / 100) * 255)
@socketio.on('button')
def openSlagboom():
    print("button clicked")
    piGPIO.set_PWM_dutycycle(servoPIN, (7.5 / 100) * 255)
    time.sleep(5)
    piGPIO.set_PWM_dutycycle(servoPIN, (2.5 / 100) * 255)
@socketio.on('getAuto')
def auto():
    state = conn.get_data(
        "SELECT Value FROM SmartParking.History WHERE SmartParking.History.SensorID = 3  ORDER BY SmartParking.History.HistoryID DESC LIMIT 6;")
    socketio.emit('giveAuto', str(state[0]['value']))
# refers to the class that works the rfid reader and the automatic barrier
parking = parkingSensor.parkingSensor(conn)
slagboom = rfidreader.rfid(conn, openSlagboom)
if __name__ == '__main__':
    socketio.run(app)
    app.run()
                                                            
