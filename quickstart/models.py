
import PIL as pillow

# Create your models here.
from django.db import models


class Locality(models.Model):
    location = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude= models.FloatField()
    height	 = models.CharField(max_length=200)
    def __str__(self):
    	return "{}" .format(self.location)

class Status(models.Model):
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)
    active = models.BooleanField()
    date = models.DateTimeField()
    verification = models.BooleanField()
    def __str__(self):
    	return "{}" .format(self.id)

class Tasbir(models.Model):
	locality = models.ForeignKey(Locality, on_delete=models.CASCADE)
	tasbir = models.ImageField(upload_to ='bin_images')

