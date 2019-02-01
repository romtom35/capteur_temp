import time
from temperatureSensor import TemperatureSensor
capteur = TemperatureSensor('28-021313bf0eaa')


type_temp = input('Quelle unite de température voulez-vous chosir (F ou C) : ')
if type_temp == 'C':
    while True:
        print(capteur.read_temp())
        time.sleep(1)
elif type_temp == 'F':
    while True:
        print(capteur.read_temp_far())
        time.sleep(1)
