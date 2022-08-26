from django.shortcuts import get_object_or_404
from .models import Player, Team
import random
import numpy as np
import joblib


def Randomteamname():
    names = ['Los Santos Lava','San Carlos Caravaners','Alamo City Armadillos', 'Swamp City Crocs','Baytown Behemoths',
    'Midwest Machiners', 'Gold City Goblins', 'Cobbleland Patrioteers', 'Island Town Exiters', 'Mountainland Marmots',
    'Prarie City Buffalo', 'Hill Region Hightoppers', 'Salt City Shippers', 'New Town Heroes', 'Lakeland Laymen',
    'Sea City Prismarine', 'Goodtown Ol Boys', 'Northland Snowshovelers']

    randomteam = random.choice(names)
    return (randomteam)



#add players to CPU team.
def CPUdraftplayer(teams):
    for team in teams:
        draftedplayer = Player.objects.filter(team='Free Agents').order_by('-2022ppg')
        if(draftedplayer.team == 'Free Agents'):
            draftedplayer.team = team
            draftedplayer.save()
        else:
            return ({'error':'Player could not be drafted, he already has a team.'})


def PredictPPG(player):
    ppg_model =  joblib.load(open('ppgpredictormodel2.0.pkl','rb'))
    playerstats = [player.age,player.mpg,player.years,player.draftPos,player.salary]
    playerstats = np.array(playerstats)
    print(playerstats)

    playerstats = playerstats.reshape(1,-1)   #We must reshape the data to fit the prediction model. Using linear regression.

    pred_ppg = ppg_model.predict(playerstats)
        

    pred_ppg = random.normalvariate(pred_ppg, 3)  #RMSE of the model is approximately 1.8
    pred_ppg = float(pred_ppg)
    pred_ppg = round(pred_ppg,2)

        

    return(pred_ppg)