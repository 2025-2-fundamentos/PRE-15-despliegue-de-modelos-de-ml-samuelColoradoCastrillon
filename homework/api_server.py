"""Minimal api_server placeholder for homework tests."""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(silent=True) or {}
    return jsonify({"prediction": None, "input": data})


if __name__ == '__main__':
    app.run(port=8000)
