import requests

# Fetch weather data from OpenWeatherMap API


def get_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': '171c5d56a4cfcfe5dd0910440da65a75',
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather_data(weather_data):
    if weather_data.get('cod') != 200:
        print("Error fetching weather data:", weather_data.get('message'))
        return

    city = weather_data.get('name')
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    weather_condition = weather_data['weather'][0]['description']

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_condition}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = "your_openweathermap_api_key"  # Replace with your actual OpenWeatherMap API key
    weather_data = get_weather_data(city, api_key)
    display_weather_data(weather_data)