import json
import requests
import os
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.conf import settings
from modules.locations.models import Place, PlaceImage

class Command(BaseCommand):
    help = "Загружает локации из JSON-файла"

    def add_arguments(self, parser):
        parser.add_argument('json_path', type=str, help='Путь к JSON-файлу (локальный или URL)')

    def handle(self, *args, **options):
        path = options['json_path']

        if path.startswith('http'):
            response = requests.get(path)
            response.raise_for_status()
            data = response.json()
        else:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)

        for item in data:
            place, created = Place.objects.get_or_create(
                name=item['title'],
                defaults={
                    'description': item['description_long'],
                    'latitude': item['coordinates']['lat'],
                    'longitude': item['coordinates']['lng'],
                }
            )

            first_image = True
            for img_url in item.get('imgs', []):
                try:
                    if img_url.startswith('media/'):
                        local_path = os.path.join(settings.BASE_DIR, img_url)
                        if os.path.exists(local_path):
                            with open(local_path, 'rb') as img_file:
                                image_content = img_file.read()
                                image_name = os.path.basename(img_url)

                                place_image = PlaceImage(place=place, is_main=first_image)
                                place_image.image.save(image_name, ContentFile(image_content))

                                if first_image:
                                    first_image = False

                                self.stdout.write(self.style.SUCCESS(f"✅ Изображение {image_name} загружено"))
                        else:
                            self.stdout.write(self.style.WARNING(f"⚠️ Файл не найден: {local_path}"))
                    else:
                        if not img_url.startswith(('http://', 'https://')):
                            img_url = 'https://' + img_url

                        img_response = requests.get(img_url)
                        img_response.raise_for_status()
                        image_name = img_url.split('/')[-1]

                        place_image = PlaceImage(place=place, is_main=first_image)
                        place_image.image.save(image_name, ContentFile(img_response.content))

                        if first_image:
                            first_image = False

                        self.stdout.write(self.style.SUCCESS(f"✅ Изображение {image_name} загружено"))

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"❌ Ошибка загрузки изображения {img_url}: {str(e)}"))
                    continue

            self.stdout.write(self.style.SUCCESS(f"✅ {place.name} загружен"))