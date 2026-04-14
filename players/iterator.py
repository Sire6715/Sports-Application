from abc import ABC, abstractmethod
from .player import Player

class Iterator(ABC):
     @abstractmethod
     def has_next(self):
          pass
     
     @abstractmethod
     def next(self):
          pass      
     
class ListIterator(Iterator):
     def __init__(self, team):
          self._players = team.players
          self._index = -1
          
     def next(self):
          self._index += 1
          t  = self._players[self._index]
          return Player(*t)
     
     def has_next(self):
          return self._index < len(self._players) - 1
          
class GeneratorIterator(Iterator):
    def __init__(self, team):
        self._players = team.players
        self._player_generator = (player for player in team.players)
        self._count = 0

    def next(self):
        self._count += 1
        t = next(self._player_generator)
        return Player(*t)

    def has_next(self):
        return self._count < len(self._players)
     
class DictIterator(Iterator):
     def __init__(self, team):
          self._players = team.players
          self._keys = list(self._players.keys())
          self._index = -1
          
     def next(self):
          self._index += 1
          key = self._keys[self._index]
          name = self._players[key]
          return Player(key, name.last_name, name.firstname)
     
     def has_next(self):
          return self ._index < len(self._players) - 1