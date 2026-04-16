import random

class ExecutivePass(object):
     _instance = None
     
     @classmethod
     def obtain(cls, holder):
          if cls._instance is None:
               cls._instance = super().__new__(cls)
               cls._instance._key = random.randint(1, 999)
               
               print("** Executive pass created, "
                     f"key = {cls._instance._key} **")
               print()
               
          cls._instance._holder = holder
          return cls._instance
     
     @classmethod
     def delete(cls):
          print("** Executive pass deleted **",
                f'key = {cls._instance._key}')
          
          cls._instance = None
          return None
     
     def __str__(self):
          return (f'holder is {self._holder}, key is {self._key}')
          
     def __new__(cls):
          raise NotImplementedError("Cannot explicitly create a singleton")
     
     def __copy__(self):
          raise NotImplementedError("Cannot copy a singleton")
     
     def __deepcopy__(self):
          raise NotImplementedError("Cannot deepcopy a singleton")