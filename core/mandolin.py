from core.instrument import Instrument
from core.mandolin_spec import MandolinSpec


class Mandolin(Instrument):
    def __init__(self, serial_number: str, price: float, spec: MandolinSpec):
        super().__init__(serial_number, price, spec)
