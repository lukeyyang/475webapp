from app import app
from flask import render_template, url_for, redirect
from .nav import nav
import serial

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')



@app.route('/setzone/<int:zonenum>')
def set_zone(zonenum): 
    if (0 <= zonenum <= 8):
        ser = serial.Serial('/dev/ttyUSB0')
        ser.write(str(zonenum))
        ser.close()
        print("Log: sent to USB port: " + str(zonenum))
    else:
        print("Warning: invalid zone number " + zonenum)
    return redirect(url_for('index'))
