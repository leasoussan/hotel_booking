from django.db import models

import datetime


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    fax = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.name}{self.location}"



class Image(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    img_name = models.CharField(max_length=100)
    image = models.URLField(max_length=300)

def __str__(self):
        return f"{self.hotel}{self.img_name}"


