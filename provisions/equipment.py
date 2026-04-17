from provision_item import ProvisionItem

BALL_COST = 5
BAT_COST = 25
GLOVE_COST = 15

class Ball(ProvisionItem):
     def __init__(self):
          super().__init__('BALL', BALL_COST)
          
class Bat(ProvisionItem):
     def __init__(self):
          super().__init__('BAT', BAT_COST)  
          
class Glove(ProvisionItem):
     def __init__(self):
          super().__init__('GLOVE', GLOVE_COST)