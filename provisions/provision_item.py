class ProvisionItem:
     def __init__(self, name, cost):
          self._name = name
          self._cost = cost
          self._provisions = None
          
     @property
     def name(self):
          return self._name
     
     @property
     def cost(self):          
          return self._cost
     
     @property
     def provisions(self):
          raise Exception('Invalid operation')
     
     def add(self, item):
          raise Exception('Invalid operation')
     
     def remove(self, item):
          raise Exception('Invalid operation')
     
     def _indent(self, indentation):
          for _ in range(indentation):
               print('   ', end='')
               
     def print_item(self, indentation):
          self._indent(indentation)
          print(f'{self.name:>6s} cost: ${self.cost}')
     
     