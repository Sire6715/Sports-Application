class Player:
     def __init__(self, player_id, first, last):
          self._player_id = player_id
          self._firstname = first 
          self._last_name = last


     @property
     def player_id(self): return self._player_id

     @property
     def firstname(self): return self._firstname

     @property
     def last_name(self): return self._last_name