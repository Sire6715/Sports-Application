from provision_group import EquipmentGroup, UniformGroup, FootWearGroup, ProvisionGroup
from equipment import Ball, Bat, Glove
from footwear import Shoes, Socks
from sunscreen import Sunscreen
from cost_report import CostReport
from uniform import Jersey, Cap, Pants

def build_cost_tree():
     equipment = EquipmentGroup()
     uniform = UniformGroup()
     footwear = FootWearGroup()
     
     equipment.add(Ball())
     equipment.add(Bat())     
     equipment.add(Glove())
     
     footwear.add(Shoes())
     footwear.add(Socks())
     
     uniform.add(Jersey())
     uniform.add(Cap())  
     uniform.add(Pants())
     uniform.add(footwear)
     
     sunscreen = Sunscreen()
     
     tree_root = ProvisionGroup("PROVISIONS")
     for item in (equipment, uniform, sunscreen):
          tree_root.add(item)
          
     return tree_root

if __name__ == '__main__':
     report = CostReport(build_cost_tree())
     report.generate_report()
          
     