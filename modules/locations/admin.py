from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from .models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    extra = 1
    fields = ('image', 'image_preview', 'is_main')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:80px;border-radius:4px;" />', obj.image.url)
        return ""
    image_preview.short_description = "Превью"


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'main_image_preview')
    inlines = [PlaceImageInline]
    fields = ('name', 'description', 'latitude', 'longitude', 'image', 'main_image_preview')
    readonly_fields = ('main_image_preview',)

    def main_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:100px;border-radius:4px;" />', obj.image.url)
        return ""
    main_image_preview.short_description = "Главное фото" 