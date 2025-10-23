import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Place, PlaceImage

def home_page(request):
    return render(request, 'locations/home.html')

def places_geojson(request):
    features = []

    for p in Place.objects.all():
        lat = float(str(p.latitude).replace(',', '.'))
        lon = float(str(p.longitude).replace(',', '.'))

        image_url = None
        if p.image:
            try:
                image_url = p.image.url
            except ValueError:
                image_url = None

        if not image_url:
            first_image = p.images.first()
            if first_image and first_image.image:
                try:
                    image_url = first_image.image.url
                except ValueError:
                    image_url = None

        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat]
            },
            "properties": {
                "name": p.name,
                "description": p.description,
                "image": image_url,
                "place_id": p.id
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

        images = []
        for img in place.images.all():
            if img.image:
                try:
                    images.append({
                        "url": img.image.url,
                        "is_main": img.is_main
                    })
                except ValueError:
                    continue

        main_image_url = None
        if place.image:
            try:
                main_image_url = place.image.url
            except ValueError:
                main_image_url = None

        data = {
            "id": place.id,
            "name": place.name,
            "description": place.description,
            "latitude": float(str(place.latitude).replace(',', '.')),
            "longitude": float(str(place.longitude).replace(',', '.')),
            "main_image": main_image_url,
            "all_images": images
        }
        return JsonResponse(data)
    except Place.DoesNotExist:
        return JsonResponse({"error": "Place not found"}, status=404)