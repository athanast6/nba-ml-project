from django.contrib import admin
from .models import Player

# Register your models here.
admin.site.register(Player)


class PlayerAdmin(admin.ModelAdmin):
   list_display=['name','ppg','predictedppg']
