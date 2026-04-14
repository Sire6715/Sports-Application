from abc import ABC, abstractmethod
from .iterator import ListIterator, GeneratorIterator, DictIterator
from collections import namedtuple

class Team(ABC):
     def __init__(self, name, players):
          self._name = name
          self._players = players
          
     @property
     def name(self): return self._name
     
     @property
     def players(self):
          return self._players
     
     @abstractmethod
     def iterator(self):
          pass
     
     
class Team_1(Team):
     def __init__(self):
          super().__init__('TEAM 1', [
               (11042, 'Rivera', 'Marco'),
               (22183, 'Okafor', 'Chidi'),
               (33294, 'Tanaka', 'Yuki'),
               (44305, 'Petrov', 'Alexei'),
               (55416, 'Mensah', 'Kwame'),
               (66527, 'Delgado', 'Rosa'),
               (77638, 'Nakamura', 'Hana'),
               (88749, 'Osei', 'Kofi'),
               (99850, 'Brennan', 'Ciara'),
          ])
          
          self._iterator = ListIterator(self)
     
     @property
     def iterator(self):         
          return self._iterator
     
     
          
class Team_2(Team):
     def __init__(self):
          super().__init__('TEAM 2', [
               (10293, 'Adeyemi', 'Tunde'),
               (20384, 'Fitzgerald', 'Nora'),
               (30475, 'Yamamoto', 'Kenji'),
               (40566, 'Diallo', 'Aminata'),
               (50657, 'Kowalski', 'Piotr'),
               (60748, 'Subramaniam', 'Priya'),
               (70839, 'Olawale', 'Bisi'),
               (80920, 'Lindqvist', 'Erik'),
               (91011, 'Ferreira', 'Lucia'),
          ])
          
          self._iterator = GeneratorIterator(self)
          self._index= -1
          
     @property
     def iterator(self):
          return self._iterator
          
class Team_3(Team):
     def __init__(self):
          super().__init__('TEAM 3', {})
          Name = namedtuple('Name', ['firstname', 'last_name'])
          self._players[13572] = Name('Abara', 'Emeka')
          self._players[24683] = Name('Thornton', 'Miles')
          self._players[35794] = Name('Vasquez', 'Elena')
          self._players[46805] = Name('Kimura', 'Sota')
          self._players[57916] = Name('Okonkwo', 'Ngozi')
          self._players[68027] = Name('Bergstrom', 'Astrid')
          self._players[79138] = Name('Farouk', 'Tariq')
          self._players[80249] = Name('Reyes', 'Camila')
          self._players[91350] = Name('Nwosu', 'Tobenna')
          
          self._iterator = DictIterator(self)
          
     @property
     def iterator(self): 
          return self._iterator