from .GuitarSpec import GuitarSpec


class Guitar:
    def __init__(self, serial_number, price, spec) -> None:
        self.serial_number = serial_number
        self.price = price
        self.spec = spec

    def get_serial_number(self) -> str:
        return self.serial_number

    def get_price(self):
        return self.price

    def set_price(self, new_price) -> None:
        self.price = new_price

    def get_spec(self) -> GuitarSpec:
        return self.spec