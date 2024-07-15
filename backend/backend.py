from flask import Flask, jsonify
from flask_cors import CORS
from modules.data_processor import process_data, get_data, get_stats

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/process')
def process():
    data, stats = process_data()
    return jsonify({"message": "Data processed successfully"})

@app.route('/data')
def data():
    return jsonify(get_data())

@app.route('/statistics')
def statistics():
    return jsonify(get_stats())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)