from distutils.log import error
from gc import get_objects
from django.shortcuts import render,redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth.models import User
from .models import Player, Team, League, Season
from .forms import LeagueForm
from .generators import Randomteamname, CPUdraftplayer, PredictPPG


import random
import pickle
import numpy as np
import joblib


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

        pred_ppg = PredictPPG(player)

        ppg2022 = player.ppg2022
        
        
        
        return render(request, 'ppg_predictor/playersprediction.html',{'playername':playername ,'predictedppg':pred_ppg,'ppg2022':ppg2022})




def simulationgame(request):
    leagues = League.objects.all()
    return render(request, 'simulationgame/simulationgame.html',{'leagues':leagues})


def viewleague(request, league_pk):
    league = get_object_or_404(League, pk=league_pk)
    teams = Team.objects.filter(league=league)
    seasons = Season.objects.filter(league=league)
        
    return render(request, 'simulationgame/viewleague.html',{'league':league,'seasons':seasons,'teams':teams})


def newleague(request):
    if request.method == 'GET':
        return render(request, 'simulationgame/newleague.html')
    else:
        try:
            newleague = League()
            newleague.leaguename=request.POST['leaguename']
            newleague.user = request.user
            newleague.save()

            newseason=Season()
            newseason.year='2023'
            newseason.league=newleague
            newseason.save()

            userteam = Team()
            userteam.teamname=request.POST['teamname']
            userteam.league=newleague
            userteam.user = request.user
            userteam.save()


            numberteams = int(request.POST['numberteams'])
            print(numberteams)
            listteams=[]

            for x in range(1,numberteams):
                randomteam = Randomteamname()

                while(randomteam in listteams):
                    randomteamname = Randomteamname()
                    if(randomteamname == randomteam):
                        continue
                    else:
                        break
                    
                listteams += [randomteam]
                newteam = Team()
                newteam.teamname=randomteam
                newteam.league=newleague
                newteam.user=get_object_or_404(User, pk=2) #2 is CPU_AI user id.
                print(newteam.user)
                newteam.save()
                x+=1
                



            league_pk=newleague.id
            return redirect('viewleague', league_pk=league_pk)
        except ValueError:
            return render(request, 'simulationgame/newleague.html', {'error':'Bad data passed, please try again.'})



def draft(request):
    if request.method == 'GET':
        return render (request, 'simulationgame/draft.html')
    else:
        try:
            player = request.POST['playername']
            draftedplayer = get_object_or_404(Player,name = player)
            currentteam= get_object_or_404(Team, user = request.user)
            print(currentteam)
            draftedplayer.team = currentteam
            draftedplayer.save()
            team_pk = currentteam.id


            #add players to cpu teams
            #find all teams NOT CONTROLLED by user
            #assign players from free agents to each team, by descending ppg
            AI_teams = Team.objects.filter(user = 2)                            #2 is CPU_AI user id.
            for team in AI_teams:
                players = Player.objects.filter(team = 'Free Agents').order_by('-ppg2022')
                cpu_pick = players.first()
                cpu_pick.teamname = team
                cpu_pick.save()


            return redirect('viewteam', team_pk=team_pk)

        except ValueError:
            return render(request, 'simulationgame/draft.html', {'error':'Bad data passed, please try again.'})


     
def viewteam(request, team_pk):
    team = get_object_or_404(Team, pk=team_pk)
    teamplayers = Player.objects.filter(team = team)
    if request.method == 'GET':
        return render(request,'simulationgame/viewteam.html',{'team':team,'teamplayers':teamplayers})

