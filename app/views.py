from app import app
from flask import render_template, url_for, redirect
from .nav import nav
import serial
import datetime

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')



@app.route('/setzone/<int:zonenum>')
def set_zone(zonenum): 
    if (0 <= zonenum <= 8):
        ser = serial.Serial('/dev/ttyUSB0', timeout = 2)
        ser.write(str(zonenum))


        response = ser.read(255)
        if (len(response) > 0):
#                print('Got: ' + response)
            with open("/home/pi/Desktop/ee459/runtime/sprinkler.log", "a") as logfd:
                d = datetime.datetime.now()
                timestr = d.strftime("%m/%d/%Y %H:%M:%S")
                logfd.write(timestr + " " + response.strip())
                logfd.write("\n")

        ser.close()
        print("Log: sent to USB port: " + str(zonenum))
    else:
        print("Warning: invalid zone number " + zonenum)
    return redirect(url_for('index'))
