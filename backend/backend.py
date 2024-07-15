from flask import Flask, jsonify
from flask_cors import CORS
from modules.data_processor import process_data, get_data, get_stats

app = Flask(__name__)
# Enable CORS only for all routes with the specific origin
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

@app.route('/process')
def process():
    data, stats = process_data()
    return jsonify({"message": "Data processed successfully"})

@app.route('/data')
def data():
    return jsonify(get_data())

@app.route('/stats')
def stats():
    response = jsonify(get_stats())
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)