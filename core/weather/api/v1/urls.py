from django.urls import path

from core.weather.api.v1.views import GetLocationWeatherInformationAPIView

urlpatterns = [
    path('get-location-weather-info/', GetLocationWeatherInformationAPIView.as_view(), name='get_location_info')
]