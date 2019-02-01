import time
from temperatureSensor import TemperatureSensor
capteur = TemperatureSensor('28-021313bf0eaa')


type_temp = input('Quelle unite de température voulez-vous chosir (F ou C) : ')
if 'C':
    while True:
        print(capteur.read_temp())
        time.sleep(1)
elif 'F':
    while True:
        print(capteur.read_temp_far())
        time.sleep(1)
