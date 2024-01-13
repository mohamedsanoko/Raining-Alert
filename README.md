# Weather Alert Notifier
This Python script provides a simple weather alert notifier using the OpenWeatherMap API and Twilio. It checks the weather forecast for a specified location and sends an SMS alert if rain is expected.

# Getting Started
  1. Clone the repository.
  2. Install dependencies(Python, Twilio).
  3. Set up environment variables for security.
  4. Run the script.

# Project structure
The main script fetches weather data from the OpenWeatherMap API, checks for rain in the forecast, and sends an SMS alert using Twilio if rain is expected.

# How It Works
  1. The script makes a request to the OpenWeatherMap API to fetch the 4-day weather forecast for     the specified location.
  2. It checks each forecast entry for the weather condition code (weather_id). If the code           indicates rain (ID < 700), the will_rain variable is set to True.
  3. If rain is expected, the Twilio client is initialized, and an SMS alert is sent to the             specified phone number.

# Customization
  **Locatioin and Forecast Period**: Update MY_LAT and MY_LONG with the desired latitude and       longitude.
    Adjust the cnt parameter in the weather_parameters dictionary to fetch a different number       of forecast entries.
    
  **Twilio SMS Alert**: Customize the SMS alert message in the 'body' parameter when creating 
    the TWILIO message.

# Notes
The script uses the OpenWeatherMap API to obtain weather forecast data. Make sure to replace the placeholder API key with your actual OpenWeatherMap API key.

Twilio is used to send SMS alerts. Ensure that you have a valid Twilio account, and replace the Twilio account SID and authentication token in the script.

The phone numbers in the script are placeholders. Update them with your actual phone numbers.
