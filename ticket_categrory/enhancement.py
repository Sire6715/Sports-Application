from ticket import Ticket

class Enhancement(Ticket):
     def __init__(self, description, price, ticket):
          super().__init__(description, price)
          self._ticket = ticket
          
     @property
     def cost(self):
          return self._price + self._ticket.cost
     
class Party(Enhancement):
     PARTY_PRICE = 25
     
     def __init__(self, ticket):
          super().__init__('VIP seating', Party.PARTY_PRICE, ticket)
          
class VIP(Enhancement):
     VIP_PRICE = 20
     
     def __init__(self, ticket):
          super().__init__('VIP seating', VIP.VIP_PRICE, ticket)
          
class Coupon(Enhancement):
     COUPON_PRICE = 5
     
     def __init__(self, ticket):
          super().__init__('drink coupon', Coupon.COUPON_PRICE, ticket)
          