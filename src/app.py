from flask import Flask, render_template
from database import Database
app = Flask(__name__)

db = Database()
@app.route('/')
def index():
    data = db.load()
    print(data)
    return render_template('index.html', data=data)