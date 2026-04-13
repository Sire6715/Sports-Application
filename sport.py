from enum import Enum

class Category(Enum):
     VARSITY = 1
     INTRAMURAL = 2
     
     def __str__(self): return self.name
     
class SportType(Enum):
     BASEBALL = 1
     FOOTBALL = 2
     VOLLEYBALL = 3
     
     def __str__(self): return self.name

class Sport:
     _CATEGORY = None
     _SPORT_TYPE = None
     
     def __init__(self, player_strategy, venue_strategy):
          self._player_strategy = player_strategy
          self._venue_strategy = venue_strategy
          
     @property
     def CATEGORY(self): return self._CATEGORY
     
     @property
     def SPORT_TYPE(self): return self._SPORT_TYPE
     
     @property
     def player_strategy(self): return self._player_strategy
     
     @property
     def venue_strategy(self): return self._venue_strategy
     
     @player_strategy.setter
     def player_strategy(self, ps):
          self._player_strategy = ps
          
     @venue_strategy.setter
     def venue_strategy(self, vs):
          self._venue_strategy = vs
          
     def recruit_players(self):
          return self._player_strategy.strategy()
     
     def reserve_venue(self):
          return self._venue_strategy.strategy()