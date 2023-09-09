import datetime as dt

import requests
from twilio.rest import Client


# Function to convert Kelvin to Celsius and Fahrenheit
def kelvin_to_celsius_and_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit


# Function to convert wind speed from meters per second to miles per hour and kilometers per hour
def wind_speed_conversion(wind_speed):
    meters_per_second_to_miles_per_hour = wind_speed * 2.237
    meters_per_second_to_kilometers_per_hour = wind_speed * 3.6
    return meters_per_second_to_miles_per_hour, meters_per_second_to_kilometers_per_hour


# Function to send weather alert via Twilio
def send_weather_alert(weather_info):
    account_sid = open("Weather_Alert_Service/account_sid.txt", "r").read()
    auth_token = open("Weather_Alert_Service/auth_token.txt", "r").read()
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=weather_info,
        from_=open("Weather_Alert_Service/twilio_phone_number.txt", "r").read(),
        to=open("Weather_Alert_Service/my_phone_number.txt", "r").read(),
    )


# Function to fetch weather information and send the alert
def main():
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = open("Weather_Alert_Service/api_key.txt", "r").read()
    CITY = "Coral Gables"
    URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

    response = requests.get(URL).json()

    temp_kelvin = response["main"]["temp"]
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_and_fahrenheit(temp_kelvin)

    feels_like_kelvin = response["main"]["feels_like"]
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_and_fahrenheit(
        feels_like_kelvin
    )

    wind_speed = response["wind"]["speed"]
    wind_speed_mph, wind_speed_kmh = wind_speed_conversion(wind_speed)

    humidity = response["main"]["humidity"]
    clouds = response["weather"][0]["main"]
    clouds_description = response["weather"][0]["description"]
    sunrise_time = dt.datetime.utcfromtimestamp(
        response["sys"]["sunrise"] + response["timezone"]
    )
    sunset_time = dt.datetime.utcfromtimestamp(
        response["sys"]["sunset"] + response["timezone"]
    )

    weather_info = f"\nWeather in {CITY}:\n"
    weather_info += f" \n"
    weather_info += f"Temperature: {temp_celsius:.2f}°C | {temp_fahrenheit:.2f}°F\n"
    weather_info += (
        f"Feels Like: {feels_like_celsius:.2f}°C | {feels_like_fahrenheit:.2f}°F\n"
    )
    weather_info += f"Humidity: {humidity:.0f}%\n"
    weather_info += f"Weather: {clouds} ({clouds_description})\n"
    weather_info += f"Wind Speed: {wind_speed_kmh:.2f} kmh | {wind_speed_mph:.2f} mph\n"
    weather_info += f"Sunrise: {sunrise_time}\n"
    weather_info += f"Sunset: {sunset_time}"

    # Send the weather information as an SMS
    send_weather_alert(weather_info)


if __name__ == "__main__":
    main()
