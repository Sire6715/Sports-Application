from READY import READY
from VALIDATING import VALIDATING
from TICKET_SOLD import TICKET_SOLD
from SOLD_OUT import SOLD_OUT

class StatesBlock:
    READY = None
    VALIDATING = None
    TICKET_SOLD = None
    SOLD_OUT = None

    @classmethod
    def initialize(cls, machine):
        cls.READY = READY(machine)
        cls.VALIDATING = VALIDATING(machine)
        cls.TICKET_SOLD = TICKET_SOLD(machine)
        cls.SOLD_OUT = SOLD_OUT(machine)

        return cls.READY