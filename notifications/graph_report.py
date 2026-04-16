import matplotlib.pyplot as plt
from .observer import Observer

class GraphReport(Observer):
    def __init__(self, reporter):
        self._reporter = reporter
        self._singles = 0
        self._doubles = 0
        self._triples = 0
        self._home_runs = 0

        reporter.attach(self)

    def _display_graph(self):
        hits = [self._singles, self._doubles, self._triples, self._home_runs]
        what = ['Singles', 'Doubles', 'Triples', 'Home Runs']

        _, ax = plt.subplots(figsize=(6, 2))
        ax.barh(what, hits, height=0.75)

        plt.title('GAME HITS GRAPH')
        plt.xticks([5, 10, 15, 20, 25, 30], [5, 10, 15, 20, 25, 30])

        for i, hit in enumerate(hits):
            ax.text(hit + 1, i, str(hit), fontsize=10, va='center', ha='left')

        plt.show()

    def update(self, player_name):
        if player_name is not None:
            event = self._reporter.current_event
            hit = event.hit

            HIT_MAP = {
                1: '_singles',
                2: '_doubles',
                3: '_triples',
                4: '_home_runs',
            }

            if hit in HIT_MAP:
                setattr(self, HIT_MAP[hit], getattr(self, HIT_MAP[hit]) + 1)
        else:
            self._display_graph()