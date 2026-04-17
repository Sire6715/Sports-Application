from provision_item import ProvisionItem

CAP_COST = 15
JERSEY_COST = 20
PANTS_COST = 35

class Cap(ProvisionItem):
     def __init__(self):
          super().__init__('CAP', CAP_COST)
          
class Jersey(ProvisionItem):
     def __init__(self):
          super().__init__('JERSEY', JERSEY_COST)
          
class Pants(ProvisionItem):
     def __init__(self):
          super().__init__('PANTS', PANTS_COST)