<<<<<<< HEAD
from django.contrib import admin
from .models import League,Team,Player,Season




class PlayerAdmin(admin.ModelAdmin):
   list_display=['name','ppg2022','predictedppg','team']

   

# Register your models here.
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Player,PlayerAdmin)
admin.site.register(Season)
=======
from django.contrib import admin
from .models import Player

# Register your models here.
admin.site.register(Player)


class PlayerAdmin(admin.ModelAdmin):
   list_display=['name','ppg','predictedppg']
>>>>>>> 39906e396b1bd00268ab3a1262cc3050faa24ec3
