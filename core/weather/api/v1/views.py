from rest_framework.views import APIView
from rest_framework.response import Response
from dotenv import load_dotenv
import os, requests

load_dotenv()

class GetLocationWeatherInformationAPIView(APIView):

    def get(self, request):
        city_name = request.data['city_name']
        data = self.get_location_weather_info(city_name)
        
        weather_info = {}
        weather_info["latitude"] = data["coord"]["lat"]
        weather_info["longitude"] = data["coord"]["lon"]
        weather_info["description"] = data["weather"][0]["description"]
        weather_info["temp_min"] = round(float(data["main"]["temp_min"] - 273.15), 3)
        weather_info["temp_max"] = round(float(data["main"]["temp_max"] - 273.15), 3)
        weather_info["wind_speed"] = data["wind"]["speed"]
        weather_info["country"] = data["sys"]["country"]
        weather_info["location"] = city_name
        weather_info["sunrise"] = data["sys"]["sunrise"]
        weather_info["sunset"] = data["sys"]["sunset"]
        return Response(weather_info)
    
    def get_location_weather_info(self, city_name):
        try:
            API_KEY = os.getenv('API_KEY')
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
            data = requests.post(url)
            return data.json()
        except requests.exceptions.Timeout:
            print("Request timed out (exceeded 5 seconds)")
