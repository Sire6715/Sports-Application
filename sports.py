from sport import Category, SportType, Sport
from player_strategy import VarsityFootballPlayers,VarsityBaseballPlayers, IntramuralBaseballPlayers, IntramuralFootballPlayers, IntramuralVolleyballPlayers
from venue_strategy import Stadium, OpenField

class VarsityBaseball(Sport):
     _CATEGORY = Category.VARSITY
     _SPORT_TYPE = SportType.BASEBALL

          
class VarsityFootball(Sport):
     _CATEGORY = Category.VARSITY
     _SPORT_TYPE = SportType.FOOTBALL
     
          
class IntramuralVolleyball(Sport):
     _CATEGORY = Category.INTRAMURAL
     _SPORT_TYPE = SportType.VOLLEYBALL
     

          
class IntramuralFootball(Sport):
     _CATEGORY = Category.INTRAMURAL
     _SPORT_TYPE = SportType.FOOTBALL
     

class IntramuralBaseball(Sport):
     _CATEGORY = Category.INTRAMURAL
     _SPORT_TYPE = SportType.BASEBALL
     
