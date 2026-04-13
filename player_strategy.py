from abc import ABC, abstractmethod

class PlayerStrategy(ABC):
     @abstractmethod
     def strategy(self): pass
     
class BaseballPlayers(PlayerStrategy):
     def strategy(self):
          return 'baseball players'
     
class FootballPlayers(PlayerStrategy):
     def strategy(self):
          return 'football players'
     
class VolleyballPlayers(PlayerStrategy):
     def strategy(self):
          return 'volleyball players'
          