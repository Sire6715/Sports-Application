from provision_item import ProvisionItem

SHOES_COST = 50
SOCKS_COST = 5

class Shoes(ProvisionItem):
     def __init__(self):
          super().__init__('SHOES', SHOES_COST)
          
class Socks(ProvisionItem):
     def __init__(self):
          super().__init__('SOCKS', SOCKS_COST)