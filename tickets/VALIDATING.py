import random
from state import Validity, State

class VALIDATING(State):
     def __init__(self, machine):
          super().__init__('VALIDATING', machine)
          
     def insert_credit_card(self):
          print("Credit card already inserted.")
          return self
          
     def check_validity(self):
          if self.card_validity == Validity.UNKNOWN:
               self.card_validity = random.choices([Validity.YES, Validity.NO], weights=[80, 20], k=1)[0]
               
               if self.card_validity == Validity.YES:
                    print("Card is valid. You may take your ticket.")
                    return self.states.TICKET_SOLD
               else:
                    print("*** Credit card rejected. Remove your card. ***")
                    
                    return self.states.READY
       
     
     def take_ticket(self):
          if self.card_validity == Validity.UNKNOWN:
               print("Still checking your credit card's validity.")
          elif self.card_validity == Validity.YES:
               print("Take your ticket.")
               print("Remove your card")
          else:
               print("*** Credit card rejected. ***")
               print("Remove your card")
          return self
     
     def remove_credit_card(self):
          if not self.card_inserted:
               print("No credit card inserted.")
               
          elif self.card_validity == Validity.NO:
               print("*** Credit card rejected. ***")
               print("No Sale.")
               
          self.card_inserted = False
          self.card_validity = Validity.UNKNOWN
          return self.states.READY