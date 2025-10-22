from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    image = models.ImageField(upload_to='places/')

    def __str__(self):
        return self.name