from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Get application status';

@app.route('/statistics')
def statistics():
    return jsonify({'Statistic':'se'})

@app.route('/rele')
def rele():
    return 'Rele state is not implemented.'

@app.route('/rele/stats')
def rele_stats():
    return jsonify({'Rele 1':'1', 
                   'Rele 2':'0', 
                   'Rele 3':'1', 
                   'Rele 4':'0'});

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')

