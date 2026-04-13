from sports import Baseball, Football, Volleyball
from venue_strategy import Stadium

def generate_report(sport):
     print(sport.SPORT_TYPE)
     print(f'       players: {sport.recruit_players()}')
     print(f'       venues: {sport.reserve_venue()}')
     print()
     
if __name__ == '__main__':
     for sport in [Baseball(), Football(), Volleyball()]:
          generate_report(sport)
          
     volleyball = Volleyball()
     volleyball.venue_strategy = Stadium()
     generate_report(volleyball)
