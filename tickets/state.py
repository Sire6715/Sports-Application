from abc import ABC, abstractmethod
from enum import Enum

class Validity(Enum):
     YES = 1
     NO = 2
     UNKNOWN = 3
     
class State(ABC):
     def __init__(self, name, machine):
          self._name = name
          self._machine = machine
          
     @property
     def name(self):
          return self._name
     
     @property
     def states(self):
          return self._machine._states_block
     
     @property
     def count(self):
          return self._machine._count
     
     @count.setter
     def count(self, new_count):
          self._machine._count = new_count
          
     @property
     def card_inserted(self):
          return self._machine._card_inserted
     
     @card_inserted.setter
     def card_inserted(self, new_card_inserted):
          self._machine._card_inserted = new_card_inserted
          
     @property
     def card_validity(self):
          return self._machine._card_validity
     
     @card_validity.setter
     def card_validity(self, new_card_validity):
          self._machine._card_validity = new_card_validity
          
     @abstractmethod
     def insert_credit_card(self):
          pass
     
     @abstractmethod
     def check_validity(self):
          pass
     
     @abstractmethod
     def take_ticket(self):
          pass
     
     @abstractmethod
     def remove_credit_card(self):
          pass