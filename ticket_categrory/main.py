from ticket import BaseTicket
from enhancement import Party, VIP, Coupon

def print_ticket(name, ticket):
     print()
     print(f"{name:>8s}'s ticket TOTAL: $"
           f"{ticket.cost:2d}")
     print("-"*30)
     
if __name__ == '__main__':
     john_ticket = BaseTicket()
     john_ticket = Party(john_ticket)
     john_ticket = VIP(john_ticket)
     john_ticket = Coupon(john_ticket)
     john_ticket = Coupon(john_ticket)
     print_ticket('John', john_ticket)
     
     mary_ticket = BaseTicket()
     mary_ticket = Party(mary_ticket)
     mary_ticket = VIP(mary_ticket)
     mary_ticket = Coupon(mary_ticket)
     mary_ticket = Coupon(mary_ticket)
     print_ticket('John', mary_ticket)
     
     leslie_ticket = BaseTicket()
     print_ticket('Leslie', leslie_ticket)
     
     sidney_ticket = BaseTicket()
     sidney_ticket = Coupon(sidney_ticket)
     sidney_ticket = VIP(sidney_ticket)
     print_ticket('Sidney', sidney_ticket)