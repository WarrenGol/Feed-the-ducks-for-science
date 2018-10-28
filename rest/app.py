from flask import Flask, request
from flask_pymongo import PyMongo

import os

app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://mongodb:27017/website"

db = PyMongo(app,
            username=os.getenv('DB_USERNAME'),
            password=os.getenv('DB_PASSWORD'),
            authSource='admin').db


@app.route('/submit', methods=['POST'])
def submit():
    data = {}
    data['time'] = request.form.get('time') # or datetime.datetime.utcnow() ?
    data['food'] = request.form.get('food')
    data['location'] = request.form.get('location')
    data['duck_count'] = request.form.get('duck_count')
    data['food_type'] = request.form.get('food_type')
    data['food_quantity'] = requst.form.get('food_quantity')

    db.duck_info.insert(data)

@app.route('/set_schedule', methods=['POST'])
def schedule():
    # todo schedule, 
    # Could create an event that inserts into mongo 
    
    # Or.. could insert into mongo once, record the date and
    # the number of times to trigger the event, then you could 
    # just calculate from that dataset how many times it would've
    # triggered.
    pass
