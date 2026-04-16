from .subject import Subject
from .event import EventMaker

class BaseballReporter(Subject):
    def __init__(self):
        super().__init__()
        self._event_maker = EventMaker()
        self._current_event = None

    @property
    def current_event(self):
        return self._current_event

    def report_hits(self):
        self._current_event = self._event_maker.next_event()

        while self._current_event is not None:
            self.notify(self._current_event.player_name)
            self._current_event = self._event_maker.next_event()

        self.notify(None)