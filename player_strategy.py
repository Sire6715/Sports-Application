from abc import ABC, abstractmethod

class PlayerStrategy(ABC):
     @abstractmethod
     def strategy(self): pass
     
     
class VolleyballPlayers(PlayerStrategy):
     def strategy(self):
          return 'volleyball players'
     
class VarsityBaseballPlayers(PlayerStrategy):
     def strategy(self):
          return 'varsity Baseball players'
class VarsityFootballPlayers(PlayerStrategy):
     def strategy(self):
          return 'varsity football players'
     
class IntramuralBaseballPlayers(PlayerStrategy):
     def strategy(self):
          return 'Intramural baseball players'
     
class IntramuralFootballPlayers(PlayerStrategy):
     def strategy(self):
          return 'Intramural football players'
class IntramuralVolleyballPlayers(PlayerStrategy):
     def strategy(self):
          return 'Intramural volleyball players'
          