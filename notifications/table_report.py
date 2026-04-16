from .observer import Observer

class TableReport(Observer):
    def __init__(self, reporter):
        self._reporter = reporter
        self._hit_map = {}

        reporter.attach(self)

    def _print_header(self):
        print()
        print('GAME HITS TABLE')
        print()
        print('Player     Outs      Singles     Doubles    Triples    Home Runs')
        print('---------------------------------------------------------------')

    def update(self, player_name):
        event = self._reporter.current_event

        if player_name is not None:
            hit = min(event.hit, 4)

            if player_name not in self._hit_map:
                self._hit_map[player_name] = 5 * [0]

            self._hit_map[player_name][hit] += 1
        else:
            self._print_header()
            for name, hits in self._hit_map.items():
                print(f'{name:7s} {hits[0]:8d} {hits[1]:11d} {hits[2]:11d} {hits[3]:11d} {hits[4]:11d}')