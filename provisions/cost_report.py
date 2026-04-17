class CostReport:
     def __init__(self, tree_root):
          self._tree_root = tree_root
          
     def generate_report(self):
          self._tree_root.print_item()