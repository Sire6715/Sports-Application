from abc import ABC, abstractmethod

class VenueStrategy(ABC):
     @abstractmethod
     def strategy(self): pass
     
class Stadium(VenueStrategy):
     def strategy(self):
          return 'stadium'
     
class OpenField(VenueStrategy):
     def strategy(self):
          return 'open field'