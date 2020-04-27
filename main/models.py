"""
    Author: Peter Murimi
"""
from django.db import models

class TopCarousel(models.Model):
    carousel_img = models.ImageField(upload_to='pics')
    image_alt = models.CharField(max_length=15)
    carousel_desc = models.CharField(max_length=35)


class OurServices(models.Model):
    service_img = models.ImageField(upload_to='services_pics')
    service_name = models.CharField(max_length=15)
    service_description = models.TextField()


class Team(models.Model):
    name = models.CharField(max_length=15)
    rank = models.CharField(max_length=10)
    personality = models.TextField()
    img = models.ImageField(upload_to='team_pics')

