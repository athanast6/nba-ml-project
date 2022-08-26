from django.forms import ModelForm
from .models import Player, League

class Playerform(ModelForm):
    class Meta:
        model = Player
        fields = ["name"]

class LeagueForm(ModelForm):
    class Meta:
        model = League
        fields = ["leaguename"]