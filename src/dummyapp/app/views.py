from flask import render_template
from app import app
from systeminfo import main
result = main.platform_specs()

@app.route('/')
def index():
    global result
    returnDict = {}
    returnDict['sysInfo'] =  result
    returnDict['user'] = 'Conor'
    returnDict['title'] = 'Home'
    return render_template("index.html", **returnDict)
