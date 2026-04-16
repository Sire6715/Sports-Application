from state import Validity, State

class SOLD_OUT(State):
     def __init__(self, machine):
          super().__init__('SOLD_OUT', machine)
          
     def insert_credit_card(self):
          print("*** Machine sold out. ***")
          print("*** Remove your credit card. ***")
          
          self.card_inserted = True
          self.card_validity = Validity.UNKNOWN
          return self
          
     def check_validity(self):
          print("*** No more tickets available. ***")
          
          if self.card_inserted:
               print("*** Remove your credit card. ***")
               
          return self
     
     def take_ticket(self):
          print("*** No more tickets available. ***")
          
          if self.card_inserted:
               print("*** Remove your credit card. ***")
               
          return self
     
     def remove_credit_card(self):
          
          if self.card_inserted:
               print("*** You've removed your credit card. ***")
               
               self.card_inserted = False
               self.card_validity = Validity.UNKNOWN
          else:
               print("*** No credit card inserted. ***")
          
          
          return self