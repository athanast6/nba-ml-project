<<<<<<< HEAD
from csv import DictReader
from django.core.management import BaseCommand

# Import the model 
from ppg_predictor.models import Player, Team, League, Season


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from player stats file"

    def handle(self, *args, **options):
    
        # Show this if the data already exist in the database
        if Player.objects.exists():
            print('player data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
            
        # Show this before loading the data into the database
        print("Loading players data")



        league=League()
        league.save()
        season=Season(year='2023',league=league)
        season.save()
        team = Team(teamname = 'Free Agents',league=league)
        team.save()

        #Code to load the data into database
        for row in DictReader(open('./statsnba2023.csv')):
            potential=(118-int(row['Age']))
            
            
            player=Player(name=row['Player'], age=row['Age'], mpg = row['MP'], years = row['YOS'],
                            draftPos=row['Draft Rank'],salary=row['2022-23'],ppg2022=row['PTS'],predictedppg = row['PTS'],
                            potential=potential,team=team)  
=======
from csv import DictReader
from django.core.management import BaseCommand

# Import the model 
from ppg_predictor.models import Player


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from player stats file"

    def handle(self, *args, **options):
    
        # Show this if the data already exist in the database
        if Player.objects.exists():
            print('player data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
            
        # Show this before loading the data into the database
        print("Loading players data")


        #Code to load the data into database
        for row in DictReader(open('./statsnba2023.csv')):
            player=Player(name=row['Player'], age=row['Age'], mpg = row['MP'], years = row['YOS'],
                            draftPos=row['Draft Rank'],salary=row['2022-23'],ppg2022=row['PTS'],predictedppg = row['PTS'])  
>>>>>>> 39906e396b1bd00268ab3a1262cc3050faa24ec3
            player.save()