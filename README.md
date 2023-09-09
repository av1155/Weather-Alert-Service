# Weather Alert Program

This Python script leverages various APIs and libraries to provide real-time weather information and send alerts using Twilio. Here's a breakdown of the key components and functions in your code:

## Table of Contents
- [Overview](#overview)
- [Functions](#functions)
- [Usage](#usage)
- [Configuration](#configuration)
- [Acknowledgments](#acknowledgments)

## Overview

This program fetches weather data for a specific city (in this case, Coral Gables) from the OpenWeatherMap API and then sends a weather alert via Twilio SMS. It provides essential weather information such as temperature, humidity, wind speed, and sunrise/sunset times.

## Functions

### `kelvin_to_celsius_and_fahrenheit(kelvin)`

This function converts temperature from Kelvin to Celsius and Fahrenheit.

### `wind_speed_conversion(wind_speed)`

This function converts wind speed from meters per second to miles per hour and kilometers per hour.

### `send_weather_alert(weather_info)`

This function sends a weather alert message using Twilio. It reads account SID, authentication token, and phone numbers from external files.

### `main()`

The `main()` function is the entry point of the program. It fetches weather data from the OpenWeatherMap API, processes the data, and then sends the weather alert via Twilio using the `send_weather_alert()` function.

## Usage

To use this program effectively, follow these steps:

1. Ensure you have the necessary API keys and credentials.
2. Customize the city by modifying the `CITY` variable in the script.
3. Prepare the required configuration files (`api_key.txt`, `account_sid.txt`, `auth_token.txt`, `twilio_phone_number.txt`, and `my_phone_number.txt`) with your specific values.
4. Run the script, and you will receive a weather alert SMS with the current weather conditions.

## Configuration

Before running the program, make sure to configure the following files with the appropriate values:

- `api_key.txt`: Your OpenWeatherMap API key.
- `account_sid.txt` and `auth_token.txt`: Twilio account SID and authentication token.
- `twilio_phone_number.txt`: Your Twilio phone number.
- `my_phone_number.txt`: The recipient phone number for the weather alert.

## Acknowledgments

This program makes use of the following libraries and APIs:

- [OpenWeatherMap API](https://openweathermap.org/): For weather data retrieval.
- [Twilio](https://www.twilio.com/): For sending SMS alerts.

Feel free to enhance it further or adapt it for other use cases. If you have any questions or need assistance, don't hesitate to reach out. Happy coding! 🌦️📲
