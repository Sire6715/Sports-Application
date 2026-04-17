from provision_item import ProvisionItem

SUNSCREEN_COST = 5

class Sunscreen(ProvisionItem):
     def __init__(self):
          super().__init__('SUNSCREEN', SUNSCREEN_COST)