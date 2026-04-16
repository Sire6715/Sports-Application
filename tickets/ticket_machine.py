from states_block import StatesBlock
from state import Validity

class TicketMachine:
     def __init__(self, count):
          self._states_block = None
          self._state = None
          
          self._count = count
          self._card_inserted = False
          self._card_validity = Validity.UNKNOWN
          
     def _insert_credit_card(self):
          self._state = self._state.insert_credit_card()
          
     def _check_validity(self):
          self._state = self._state.check_validity()
          
     def _take_ticket(self):
          self._state = self._state.take_ticket()
          
     def _remove_credit_card(self):
          self._state = self._state.remove_credit_card()
          
     def run(self):
          self._states_block = StatesBlock()
          self._state = StatesBlock.initialize(self)
          
          command = -1
          
          while command != 0:
               print()
               print("1. Insert credit card, 2. Check card validity, 3. Take ticket, 4. Remove credit card, 0. Exit")
               command = int(input("Enter command: "))
               
               match command:
                    case 1: self._insert_credit_card()
                    case 2: self._check_validity()     
                    case 3: self._take_ticket()
                    case 4: self._remove_credit_card()
                    
                    case 0: print("Exiting...")
                    case _: print("Invalid command")