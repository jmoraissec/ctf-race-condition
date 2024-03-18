from flask import Flask
from flask import render_template
from flask import request
import os

app = Flask(__name__)
ACTIVE = 50
PENDING = 51
y = 51

@app.route('/', methods = ['GET'])
def index():
    result = f"<table><tr><td>ACTIVE:</td><td>{ACTIVE}</td></tr><tr><td>PENDING:</td><td>{PENDING}</td></tr></table>"
    return render_template('index.html', result=result)

def log_operation(name):
    for i in range(0,50000000):   # tune this value to make the race condition more likely according to your CPU power
        pass

def set(y):
    global ACTIVE
    ACTIVE = y
def wait_set(y):
    global PENDING
    PENDING = y

def run_function(input):
    global y
    y = int(input)
    if y > ACTIVE:
        log_operation("NEW_PENDING_VALUE")
        wait_set(y)
    else:
        log_operation("NEW_ACTIVE_VALUE")
        set(y)

@app.route('/', methods = ['POST'])
def run():
    input = request.form['number']
    run_function(input)
    result = f"<table><tr><td>ACTIVE:</td><td>{ACTIVE}</td></tr><tr><td>PENDING:</td><td>{PENDING}</td></tr></table>"
    if ACTIVE > PENDING:
        result += os.getenv("FLAG")
    return render_template('index.html', result=result)

app.run(host='0.0.0.0', port=80)
