from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

@app.route('/data')
def data():
    return{}

# Executes flask in debug mode
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)