from django.contrib import admin
from .models import Place, PlaceImage

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1
    fields = ('image', 'is_main')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')
    inlines = [PlaceImageInline]
