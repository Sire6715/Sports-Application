from abc import ABC, abstractmethod

class Ticket(ABC):
     def __init__(self, description, price):
          self._description = description
          self._price = price
          
          self._print_ticket()
          
     @property
     @abstractmethod
     def cost(self):
          pass 
     
     def _print_ticket(self):
          print(f'{self._description:>17s} price: $'
                f'{self._price:2d}')
          
class BaseTicket(Ticket):
     BASE_PRICE = 30
     
     def __init__(self):
          super().__init__('base ticket', BaseTicket.BASE_PRICE)
          
     @property
     def cost(self):
          return BaseTicket.BASE_PRICE
          