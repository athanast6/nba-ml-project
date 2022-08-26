<<<<<<< HEAD
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
=======
from django.forms import ModelForm
from .models import Player

class Playerform(ModelForm):
    class Meta:
        model = Player
        fields = ["name"]
>>>>>>> 39906e396b1bd00268ab3a1262cc3050faa24ec3
