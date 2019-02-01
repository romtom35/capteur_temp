import RPi.GPIO as GPIO
import time
class Led:
    def __init__(self, status, broche):
        self.status = status
        self.broche = broche
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.broche, GPIO.OUT)


    def led_status(self):
        if (self.status == 'on'):
            GPIO.output(self.broche, GPIO.HIGH)
        elif (self.status == 'off'):
            GPIO.output(self.broche, GPIO.LOW)
        else:
            return 'Erreur de manipulation'
    def on(self):
        GPIO.output(self.broche, GPIO.HIGH)

    def off(self):
        GPIO.output(self.broche, GPIO.LOW)

    def blink(self):
        i=0
        while i < 5:
            GPIO.output(self.broche, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(self.broche, GPIO.LOW)
            time.sleep(1)
            i=i+1