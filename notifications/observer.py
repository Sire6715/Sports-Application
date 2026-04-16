from abc import ABC, abstractmethod

class Observer(ABC):
     @abstractmethod
     def update(self, player_name):
          pass