from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    image = models.ImageField(upload_to='places/', blank=True, null=True)

    def __str__(self):
        return self.name

class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='places/')
    is_main = models.BooleanField(default=False)
    position = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['position']

    def save(self, *args, **kwargs):
        if self.is_main:
            PlaceImage.objects.filter(place=self.place, is_main=True).exclude(pk=self.pk).update(is_main=False)
            self.place.image = self.image
            self.place.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.place.name} - изображение"
