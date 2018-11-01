from flask import Flask, request, redirect
from flask_pymongo import PyMongo

import os

app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://mongodb:27017/website"

db = PyMongo(app,
            username=os.getenv('DB_USERNAME'),
            password=os.getenv('DB_PASSWORD'),
            authSource='admin').db


@app.route('/submit-data', methods=['POST'])
def submit():
    data = {}
    data['time'] = request.form.get('time')
    data['food'] = request.form.get('food')
    data['location'] = request.form.get('location')
    data['duck_count'] = float(request.form.get('duck_count'))
    data['food_type'] = request.form.get('food_type')
    data['food_quantity'] = float(request.form.get('food_quantity'))
    data['repeat'] = bool(request.form.get('repeat'))

    db.duck_info.insert(data)

    return redirect('/', code=302)
