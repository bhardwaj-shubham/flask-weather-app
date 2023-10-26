from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_weather():
    return render_template('index.html')
