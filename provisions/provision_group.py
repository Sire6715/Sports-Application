from provision_item import ProvisionItem

class ProvisionGroup(ProvisionItem):
     def __init__(self, name):
          self._name = name
          self._provisions = []
          
     @property
     def name(self):
          return self._name
     
     @property
     def provisions(self):
          return self._provisions
     
     @property
     def cost(self):
          cost = 0
          for item in self._provisions: 
               cost += item.cost
          return cost
     
     def add(self, item):
          self._provisions.append(item)
          
     def remove(self, item):
          self._provisions.remove(item)
          
     def print_item(self, indentation=0):
          self._indent(indentation)
          print(self._name)
          
          for item in self._provisions:
               item.print_item(indentation + 1)
               
          self._indent(indentation)
          print(f'{self._name} total cost: ${self.cost}')
          
class EquipmentGroup(ProvisionGroup):
     def __init__(self):
          super().__init__('EQUIPMENT')
          
class UniformGroup(ProvisionGroup):
     def __init__(self):
          super().__init__('UNIFORM')
          
class FootWearGroup(ProvisionGroup):
     def __init__(self):
          super().__init__('FOOTWEAR')
     