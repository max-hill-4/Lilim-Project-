from flask import Flask, render_template
import datahandler as dt

app = Flask(__name__)

data = {'bench' : dt.repMaxList('Bench Press'),'squat' : dt.repMaxList('Squat'), 'deadlift' : dt.repMaxList('Deadlift')}

@app.route('/')
def index():
    return render_template('index.html',data=data)
