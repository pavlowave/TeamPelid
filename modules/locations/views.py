import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Place

def home_page(request):
    return render(request, 'locations/home.html')

def places_geojson(request):
    features = []

    for p in Place.objects.all():
        lat = float(str(p.latitude).replace(',', '.'))
        lon = float(str(p.longitude).replace(',', '.'))

        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat]
            },
            "properties": {
                "name": p.name,
                "description": p.description,
                "image": p.image.url
            }
        })

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return JsonResponse(geojson)


def place_detail(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
        data = {
            "id": place.id,
            "name": place.name,
            "description": place.description,
            "latitude": float(str(place.latitude).replace(',', '.')),
            "longitude": float(str(place.longitude).replace(',', '.')),
            "image": place.image.url
        }
        return JsonResponse(data)
    except Place.DoesNotExist:
        return JsonResponse({"error": "Place not found"}, status=404)