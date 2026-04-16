from state import Validity, State

class TICKET_SOLD(State):
     def __init__(self, machine):
          super().__init__('TICKED_SOLD', machine)
          
     def insert_credit_card(self):
          print("Credit card already inserted.")
          return self
          
     def check_validity(self):
          print("Take the ticket that you just bought.")
          
          return self
     
     def take_ticket(self):
          print("Remove your card.")
          print("Enjoy your game!")
          
          self.count -= 1
          if self.count > 0:
               return self.states.READY
          else: 
               return self.states.SOLD_OUT
     
     def remove_credit_card(self):
          print("First take your ticket.")
          
          return self