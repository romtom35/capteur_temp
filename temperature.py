from flask import Flask
app = Flask(__name__)
from flask import render_template
import time
from temperatureSensor import TemperatureSensor
from led import Led
capteur = TemperatureSensor('28-021313bf0eaa')
led_bleue = Led('off', 24)
led_rouge = Led('off', 18)

@app.route('/')
def index():
    return render_template('temperature.html')

@app.route('/type_temp/<C_F>')
def type_temp(C_F):
    if C_F == 'celcius':
        temp_c = capteur.read_temp()
        if temp_c <= 15:
            led_bleue.on()
        elif temp_c >= 30:
            led_rouge.on()
        elif temp_c > 15 and temp_c<30:
            led_bleue.off()
            led_rouge.off()
        return render_template('temperature.html', temp_c=temp_c)

    elif C_F == 'farenheit':
        farenheit = capteur.read_temp_far()
        return render_template('temperature.html', farenheit=farenheit)
