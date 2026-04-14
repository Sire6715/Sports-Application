class TeamReport:
     def print(self, team):
          print()
          print(f'{team.name} Players')
          print('-----------------')
          
          it = team.iterator
          
          while it.has_next():
               player = it.next()
               print(f'{player.player_id} {player.last_name}, {player.firstname}')
           
           