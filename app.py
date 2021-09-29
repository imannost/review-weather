import json
import requests
from datetime import date, timedelta

from flask import Flask, request

import config
import localmath

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/weather")
def show_weather():
    city = request.args.get('city')
    n_days = int(request.args.get('days'))
    end_date = date.today()
    start_date = end_date - timedelta(days=n_days) + 1

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
            "average": localmath.count_average(temperature_c),
            "median": localmath.count_median(temperature_c),
            "min": localmath.count_min(temperature_c),
            "max": localmath.count_max(temperature_c)
        },
        "humidity": {
            "average": localmath.count_average(humidity),
            "median": localmath.count_median(humidity),
            "min": localmath.count_min(humidity),
            "max": localmath.count_max(humidity)
        },
        "pressure_mb": {
            "average": localmath.count_average(pressure_mb),
            "median": localmath.count_median(pressure_mb),
            "min": localmath.count_min(pressure_mb),
            "max": localmath.count_max(pressure_mb)
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

    response = requests.request("GET", url, headers=config.headers, params=query_string)

    return response.json()
