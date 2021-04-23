from flask import Flask, render_template
from database import Database
from pychartjs import BaseChart, ChartType, Color
from cccpchart import CccpChart

app = Flask(__name__)

db = Database()

@app.route('/')
def index():
    coin_data = db.load()
    NewChart = CccpChart()
    NewChart.options.indexAxis = 'y'
    ChartJSON = NewChart.get()
    return render_template('index.html', data=coin_data, chartJSON=ChartJSON)