from django.contrib import admin
from .models import League,Team,Player,Season




class PlayerAdmin(admin.ModelAdmin):
   list_display=['name','ppg2022','predictedppg','team']

   

# Register your models here.
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Player,PlayerAdmin)
admin.site.register(Season)