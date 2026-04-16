import random

class Event:
    def __init__(self, player_name, hit):
        self._player_name = player_name
        self._hit = hit

    @property
    def player_name(self):
        return self._player_name

    @property
    def hit(self):
        return self._hit


class EventMaker:
    def __init__(self):
        self._name_index = -1
        self._outs = 0
        self._players_name = ('Al', 'Beth', 'Charlie', 'Diana', 'Eddie', 'Fiona', 'George', 'Hannah', 'Ian')
        self._hit_weights = [55, 20, 13, 7, 5]

    def next_event(self):
        if self._outs < 27:
            hit = random.choices([0, 1, 2, 3, 4], weights=self._hit_weights, k=1)[0]

            if hit == 0:
                self._outs += 1

            self._name_index = (self._name_index + 1) % len(self._players_name)
            return Event(self._players_name[self._name_index], hit)

        return None