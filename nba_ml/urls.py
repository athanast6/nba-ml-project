<<<<<<< HEAD
"""nba_ml URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ppg_predictor.views import ppgpredictor, nbaplayersprediction, home, simulationgame, newleague, draft, viewleague, viewteam

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',home,name='home'),
    
    path('ppgpredictor/', ppgpredictor, name='ppgpredictor'),
    path('nbaplayersprediction/', nbaplayersprediction, name ='nbaplayersprediction'),

    path('simulationgame/', simulationgame, name='simulationgame'),
    path('simulationgame/newleague/', newleague, name='newleague'),
    path('simulationgame/draft/', draft, name='draft'),

    path('simulationgame/viewleague/<int:league_pk>', viewleague, name = 'viewleague'),
    path('simulationgame/viewteam/<int:team_pk>', viewteam, name='viewteam'),






]
=======
"""nba_ml URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ppg_predictor.views import ppgpredictor, nbaplayersprediction, home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',home,name='home'),
    
    path('ppgpredictor/', ppgpredictor, name='ppgpredictor'),

    path('nbaplayersprediction/', nbaplayersprediction, name ='nbaplayersprediction'),





]
>>>>>>> 39906e396b1bd00268ab3a1262cc3050faa24ec3
