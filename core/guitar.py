from core.guitar_spec import GuitarSpec
from core.instrument import Instrument


class Guitar(Instrument):
    def __init__(self, serial_number: str, price: float, spec: GuitarSpec):
        super().__init__(serial_number, price, spec)
