# Web service on Python

The web service receives weather data from public API and aggregates it, after that it returns the result. The information which service gives you:
* temperature
* humidity
* pressure, 

and their:
- average
- minimal
- maximal
- median

In this service, [Visual Crossing Weather](https://rapidapi.com/visual-crossing-corporation-visual-crossing-corporation-default/api/visual-crossing-weather/) was used as a public API. 

### Available Scripts

Install reqrequirements:
```python -m pip install -r requirements.txt```

Change **API key** in your own before you start

Use command line to change the directory
and start the service ```flask run```

### Formats
**Request's format:**
``` GET /weather?city=<city>&days=<n> ```, where n - number of days 
                                 
**Result's format:**
```
{
 "city": "Saint-Petersburg",
 "from": "2021-09-10",
 "to": "2021-09-15",
 "temperature_c": {
   "average": 25.0,
   "median": 24.5,
   "min": 20.1,
   "max": 29.3
 },
 "humidity": {
   "average": 55.4,
   "median": 58.1,
   "min": 43.1,
   "max": 82.4
 },
 "pressure_mb": {
   "average": 1016.0,
   "median": 1016.5,
   "min": 1015.1,
   "max": 1017.3
 }
}
```


