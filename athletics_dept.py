from sport import Category, SportType
from abc import ABC, abstractmethod
from sports import VarsityBaseball, VarsityFootball, IntramuralBaseball, IntramuralVolleyball, IntramuralFootball


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
                    return VarsityBaseball()
               case SportType.FOOTBALL:
                    return VarsityFootball()
               case _:
                    return None;
               
class IntramuralDept(AthleticsDept):
     def create_sport(self, sport_type):
          match sport_type:
               case SportType.BASEBALL:
                    return IntramuralBaseball()
               case SportType.FOOTBALL:
                    return IntramuralFootball()
               case SportType.VOLLEYBALL:
                    return IntramuralVolleyball()