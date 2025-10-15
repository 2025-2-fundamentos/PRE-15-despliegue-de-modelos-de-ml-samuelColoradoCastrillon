"""Minimal web_app placeholder for homework tests."""

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    app.run(port=5000)
