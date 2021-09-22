import json
from datetime import date, timedelta
from flask import Flask, request
import requests
import numpy as np

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/weather")
def show_weather():
    city = request.args.get('city')
    n_days = int(request.args.get('days'))
    end_date = date.today()
    start_date = end_date - timedelta(days=n_days)

    response = get_weather(city, start_date.__str__(), end_date.__str__())

    temperature_c = [[] for _ in range(n_days)]
    humidity = [[] for _ in range(n_days)]
    pressure_mb = [[] for _ in range(n_days)]
    for n in range(0, n_days):
        temperature_c[n] = float("{0:.1f}".format(response["locations"][city]["values"][n]["temp"]))
        humidity[n] = float("{0:.1f}".format(response["locations"][city]["values"][n]["humidity"]))
        pressure_mb[n] = float("{0:.1f}".format(response["locations"][city]["values"][n]["sealevelpressure"]))

    weather = {
        "city": city,
        "from": start_date.__str__(),
        "to": end_date.__str__(),
        "temperature_c": {
            "average": round(np.average(temperature_c), 1),
            "median": np.median(temperature_c),
            "min": np.min(temperature_c),
            "max": np.max(temperature_c)
        },
        "humidity": {
            "average": round(np.average(humidity), 1),
            "median": np.median(humidity),
            "min": np.min(humidity),
            "max": np.max(humidity)
        },
        "pressure_mb": {
            "average": round(np.average(pressure_mb), 1),
            "median": np.median(pressure_mb),
            "min": np.min(pressure_mb),
            "max": np.max(pressure_mb)
        }
    }

    return json.dumps(weather, indent=4)


def get_weather(city, start_date, end_date):
    url = "https://visual-crossing-weather.p.rapidapi.com/history"

    query_string = {"startDateTime": start_date,
                    "aggregateHours": "24",
                    "location": city,
                    "endDateTime": end_date,
                    "unitGroup": "metric",
                    "contentType": "json"}

    headers = {
        'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com",
        'x-rapidapi-key': "your-own-API-key"
    }

    response = requests.request("GET", url, headers=headers, params=query_string)

    return response.json()
