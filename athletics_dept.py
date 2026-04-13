from sport import Category, SportType
from sports import VarsityBaseball, VarsityFootball, IntramuralBaseball, IntramuralVolleyball, IntramuralFootball


class AthleticsDept:
     def generate_report(self, which):
          sport = None
          
          match which:
               case [Category.VARSITY, SportType.BASEBALL]:
                    sport = VarsityBaseball()
               case [Category.VARSITY, SportType.FOOTBALL]:
                    sport = VarsityFootball()
               case [Category.INTRAMURAL, SportType.BASEBALL]:
                    sport = IntramuralBaseball()
               case [Category.INTRAMURAL, SportType.FOOTBALL]:
                    sport = IntramuralFootball()
               case [Category.INTRAMURAL, SportType.VOLLEYBALL]:
                    sport = IntramuralVolleyball()
                    
          print(f'{sport.CATEGORY} {sport.SPORT_TYPE}')
          print(f'       players: {sport.recruit_players()}')
          print(f'            venue: {sport.reserve_venue()}')
          print()