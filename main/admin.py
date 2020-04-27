"""
    Author: Peter Murimi
"""
from django.contrib import admin
from .models import TopCarousel, OurServices, Team

admin.site.register(TopCarousel)
admin.site.register(OurServices)
admin.site.register(Team)

# Register your models here.
