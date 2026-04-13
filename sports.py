from sport import Sport
from player_strategy import BaseballPlayers, FootballPlayers, VolleyballPlayers
from venue_strategy import Stadium, OpenField

class Baseball(Sport):
     _SPORT_TYPE = 'BASEBALL'
     
     def __init__(self):
          super().__init__(BaseballPlayers(), Stadium())
          
class Football(Sport):
     _SPORT_TYPE = "FOOTBALL"
     
     def __init__(self):
          super().__init__(FootballPlayers(), Stadium())
          
class Volleyball(Sport):
     _SPORT_TYPE = 'VOLLEYBALL'
     
     def __init__(self):
          super().__init__(VolleyballPlayers(), OpenField())