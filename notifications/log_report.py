from .observer import Observer

class LogReport(Observer):
     def __init__(self, reporter):
          self._reporter = reporter
          self._count = 0

          self._reporter.attach(self)

          print('GAME HITS LOG')
          print()

     def update(self, player_name):
          if player_name is None:
               return

          event = self._reporter.current_event
          hit = event.hit

          HIT_LABELS = {
               0: 'an out',
               1: 'a single',
               2: 'a double',
               3: 'a triple',
          }

          what = HIT_LABELS.get(hit, 'a home run')
          self._count += 1
          print(f'{self._count:2d}. {player_name:7s} hit {what}')