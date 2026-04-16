from .observer import Observer

class FanClubReport(Observer):
    def __init__(self, reporter, idol):
        self._reporter = reporter
        self._idol = idol
        self._what = None
        self._reporter.attach(self)

    def print_bulletin(self):
        print()
        print('FAN CLUB BULLETIN')
        print(f'The first at-bat by {self._idol} resulted in {self._what}')

    def update(self, player_name):
        if player_name == self._idol:
            HIT_LABELS = {
                0: 'an out',
                1: 'a single',
                2: 'a double',
                3: 'a triple',
            }

            event = self._reporter.current_event
            hit = event.hit
            self._what = HIT_LABELS.get(hit, 'a home run')
            self._reporter.detach(self)