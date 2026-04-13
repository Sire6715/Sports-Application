class Sport:
     _SPORT_TYPE = ''
     
     def __init__(self, player_strategy, venue_strategy):
          self._player_strategy = player_strategy
          self._venue_strategy = venue_strategy
          
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