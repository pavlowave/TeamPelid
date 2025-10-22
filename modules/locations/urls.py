from django.urls import path
from modules.locations.views import home_page, places_geojson, place_detail

urlpatterns = [
    path('home/', home_page, name='home_page'),
    path('places-geojson/', places_geojson, name='places_geojson'),
    path('places/<int:place_id>/', place_detail, name='place_detail'),
]