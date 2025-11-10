import requests
import json

class WeatherService:
    def __init__(self):
        self.api_key = "your_api_key_here"  # You can get free API key from openweathermap.org
        self.base_url = "http://api.openweathermap.org/data/2.5"
    
    def get_weather(self, location=None):
        """Get weather information"""
        if not location:
            location = "London"
        
        # Mock weather data for demo (no API key needed)
        weather_data = {
            'location': location.title(),
            'temperature': 22,
            'description': 'partly cloudy',
            'humidity': 65,
            'wind_speed': 12
        }
        
        return weather_data
    
    def format_weather_response(self, weather_data):
        """Format weather data into natural language response"""
        return (f"In {weather_data['location']}, it's currently {weather_data['temperature']}°C "
               f"with {weather_data['description']}. Humidity is {weather_data['humidity']}% "
               f"and wind speed is {weather_data['wind_speed']} km/h.")