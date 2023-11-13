import datetime
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Access API key
api_key = os.getenv('WEATHER_API_KEY')


@app.route('/', methods=['GET'])
def get_weather():
    current_date = datetime.date.today().strftime("%d-%m-%Y")
    return render_template('index.html', current_date=current_date)


@app.route('/', methods=['POST'])
def find_weather():
    city_name = request.form['city']

    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric")

    if response.status_code != 200:
        return {"error": "City not found"}

    data = response.json()
    icon_code = data['weather'][0]['icon']
    icon_url = "https://openweathermap.org/img/w/" + icon_code + ".png";
    weather_data = {'city': str(data['name'], ), 'temperature': str(data['main']['temp'], ),
                    'description': str(data['weather'][0]['description'])}
    current_date = datetime.date.today().strftime("%d-%m-%Y")
    return render_template('index.html', current_date=current_date, weather_data=weather_data, icon_url=icon_url)
