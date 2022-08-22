from distutils.log import error
from gc import get_objects
from django.shortcuts import render,redirect, get_object_or_404
from django.db import IntegrityError
from .models import Player


import random
import pickle
import numpy as np


def home(request):
    return render(request, 'ppg_predictor/home.html')

def ppgpredictor(request):
    if(request.method == 'GET'):
        return render(request, 'ppg_predictor/ppgpredictor.html')
    else:
        try:
            return redirect('home')
        except IntegrityError:
            return render(request, 'ppg_predictor/home.html')




def nbaplayersprediction(request):
    if(request.method == 'GET'):
        playername = request.GET.get('playername') 
        print(playername)
        player = get_object_or_404(Player, name = playername)

        if player == None:
            return render(request, 'ppg_predictor/ppgpredictor.html',{'error':'Player Not Found, Please Try Again'})

        ppg_model =  pickle.load(open('ppgpredictormodel2.0.sav','rb'))

        playerstats = [player.age,player.mpg,player.years,player.draftPos,player.salary]
        playerstats = np.array(playerstats)
        print(playerstats)

        playerstats = playerstats.reshape(1,-1)   #We must reshape the data to fit the prediction model. Using linear regression.

        pred_ppg = ppg_model.predict(playerstats)
        

        pred_ppg = random.normalvariate(pred_ppg, 1.8)  #RMSE of the model is approximately 1.8
        pred_ppg = float(pred_ppg)
        pred_ppg = round(pred_ppg,2)

        ppg2022 = player.ppg2022

        

        
        return render(request, 'ppg_predictor/playersprediction.html',{'playername':playername ,'predictedppg':pred_ppg,'ppg2022':ppg2022})




    


 












