from flask import Flask
app = Flask(__name__)
from flask import render_template
import time
from temperatureSensor import TemperatureSensor
capteur = TemperatureSensor('28-021313bf0eaa')

@app.route('/')
def index():
    return render_template('temperature.html')

@app.route('/type_temp/<C_F>')
def type_temp(C_F):
    if C_F == 'celcius':
        temp_c = capteur.read_temp()
        return render_template('temperature.html', temp_c=temp_c)
    elif C_F == 'farenheit':
        farenheit = capteur.read_temp_far()
        return render_template('temperature.html', farenheit=farenheit)
