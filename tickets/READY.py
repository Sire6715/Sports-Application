from state import Validity, State

class READY(State):
     def __init__(self, machine):
          super().__init__('READY', machine)
          
          
     def insert_credit_card(self):
          if not self.card_inserted:
               print("Validating your credit card...")
               
               self.card_inserted = True
               self.card_validity = Validity.UNKNOWN
               return self.states.VALIDATING
          elif self.card_validity == Validity.NO:
               print("*** Credit card rejected. ***")
               print("Remove your card")   
               return self          
          else :
               print("Credit card already inserted.")
               return self
          
     def check_validity(self):
          if not self.card_inserted:
               print("Insert your credit card first.")
          elif self.card_validity == Validity.UNKNOWN:
               print("Still validating your card...")
          elif self.card_validity == Validity.YES:
               print("Card is valid. You may take your ticket.")
          else:
               print("*** Credit card rejected. Remove your card. ***")
          return self
     
     def take_ticket(self):
          if not self.card_inserted:
               print("First insert your credit card.")
          elif self.card_validity == Validity.UNKNOWN:
               print("Still checking your credit card's validity.")
          elif self.card_validity == Validity.YES:
               print("Take your ticket.")
               print("Remove your card")
          else:
               print("*** Credit card rejected. ***")
               print("Remove your card")
          return self
     
     def remove_credit_card(self):
          if self.card_inserted:
               print("You've removed your credit card.")
               self.card_inserted = False
               self.card_validity = Validity.UNKNOWN
          else:
               print("No credit card inserted.")
          return self
          