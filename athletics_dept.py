from sport import Category, SportType
from abc import ABC, abstractmethod
from sports import VarsityBaseball, VarsityFootball, IntramuralBaseball, IntramuralVolleyball, IntramuralFootball
from provisions_factory import VarsityFactory, IntramuralFactory


class AthleticsDept(ABC):
     @abstractmethod
     def create_sport(self, sport_type):
          pass
     
     def generate_report(self, sport_type):
          sport = self.create_sport(sport_type)
          
          print(f'{sport.CATEGORY} {sport.SPORT_TYPE}')
          print(f'  players: {sport.recruit_players()}')
          print(f'       venue: {sport.reserve_venue()}')
          print()
          
class VarsityDept(AthleticsDept):
     def create_sport(self, sport_type):
          match sport_type:
               case SportType.BASEBALL:
                    return VarsityBaseball(VarsityFactory())
               case SportType.FOOTBALL:
                    return VarsityFootball(VarsityFactory())
               case _:
                    return None;
               
               
class IntramuralDept(AthleticsDept):
     def create_sport(self, sport_type):
          match sport_type:
               case SportType.BASEBALL:
                    return IntramuralBaseball(IntramuralFactory())
               case SportType.FOOTBALL:
                    return IntramuralFootball(IntramuralFactory())
               case SportType.VOLLEYBALL:
                    return IntramuralVolleyball(IntramuralFactory())
               case _:
                    return None;