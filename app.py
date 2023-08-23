from flask import Flask, render_template, jsonify
import datahandler as dt
import json

app = Flask(__name__)

bench = {'data' : dt.repMaxList('Bench Press'), 'date' : dt.dateList('Bench Press')}
squats = {'data' : dt.repMaxList('Squat'), 'date' : dt.dateList('Squat')}
deadlift = {'data' : dt.repMaxList('Deadlift'), 'date' : dt.dateList('Deadlift')}


@app.route('/')
def index():
    return render_template('index.html', bench=bench, squats=squats, deadlift=deadlift)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(bench)