from django.forms import ModelForm
from .models import Player

class Playerform(ModelForm):
    class Meta:
        model = Player
        fields = ["name"]