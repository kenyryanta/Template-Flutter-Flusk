from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Izinkan CORS untuk semua domain

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({
        "status": "success",
        "message": "API berjalan!",
        "data": "Ini adalah data dari Flask"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Wajib gunakan 0.0.0.0
