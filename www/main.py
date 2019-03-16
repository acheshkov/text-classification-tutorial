#!flask/bin/python
import os
from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd
from joblib import dump, load

app = Flask(__name__)
model = load('./model.joblib')


@app.route('/status')
def index():
    return jsonify({'status': 'ok'})

@app.route('/classify', methods=['POST'])
def get_prediction():
    json_body = request.get_json(force=True)
    print("content", json_body)
    if (json_body is None or json_body.get('text') is None):
        return jsonify("Can't handle"), 404

    
    prediction = model.predict([json_body['text']]).tolist()[0]

    return jsonify({'predicted_class': prediction})

if __name__ == '__main__':
    if os.environ['ENVIRONMENT'] == 'production':
        app.run(port=80, host='0.0.0.0')
    if os.environ['ENVIRONMENT'] == 'local':
        app.run(port=3000, host='0.0.0.0')

