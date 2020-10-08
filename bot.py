import json
from botocore.vendored import requests
import datetime
def lambda_handler(event, context):
    City = event["currentIntent"]["slots"]["City"]
    r = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params={"q": City , "appid":"4fd97cb7f3ba6237a199d3f80311c875"} )
    data = r.json()
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
   
    output = 'The weather today is: {description} with Temperature: {temperature} , Pressure: {pressure} , Humidity: {humidity} and Wind speed: {wind_speed} '.format(description=description, temperature=temperature, pressure=pressure, humidity=humidity, wind_speed=wind_speed)
    return {
        "sessionAttributes": event["sessionAttributes"],
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": output
            }
        }
    }