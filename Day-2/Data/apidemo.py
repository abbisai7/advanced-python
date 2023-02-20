#requests,urllib3
#pip install requests

import requests
import json

url ="http://api.openweathermap.org/data/2.5/weather?q=chittoor&units=imperial&appid=ca3f6d6ca3973a518834983d0b318f73"

response = requests.get(url)
print(response.text)
print(response.headers['Content-Type'])
report = json.loads(response.text)
print(type(report))
print(report)
desc = report['weather'][0]["description"]
print(desc)