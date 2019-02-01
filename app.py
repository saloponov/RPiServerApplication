from flask import Flask
from flask import jsonify


try:
    import RPi.GPIO as GPIO
except:
    print("Error importing RPi.GPIO! Probably - Use sudo.")
from time import sleep


GPIO.setmode(GPIO.BCM)
app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome! For more information about services visit https://github.com/saloponov/RPiServerApplication.';

@app.route('/statistics')
def statistics():
    return jsonify({'Statistic':'se'})

@app.route('/relay/input/<int:pin>')
def rele(pin):
    #GPIO.setup(pin, GPIO.IN)
    return jsonify(GPIO.input(pin))

@app.route('/relay/output/<int:pin>/<int:value>')
def rele_set(pin, value):
    GPIO.cleanup(pin)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH if value else GPIO.LOW)
    return str(pin) + " = " + str(GPIO.input(pin))
    

#if name == 'main':
#    app.run(debug = True, host = '0.0.0.0')
    
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')


