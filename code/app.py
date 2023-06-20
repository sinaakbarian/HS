from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/timestamp')
def get_timestamp():
    import time
    return jsonify({'timestamp': int(time.time())})

@app.route('/readdata', methods=['POST'])
def read_data():
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost', port=8000)
