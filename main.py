from enum import Enum
from abc import ABC, abstractmethod

class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"

class TypeG(Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "electric"

class Wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "cocobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"

class Instrument(ABC):
    def __init__(self, serialNumber, price, spec):
        self.serialNumber = serialNumber
        self.price = price
        self.spec = spec

    def getSerialNumber(self):
        return self.serialNumber

    def getPrice(self):
        return self.price

    def setPrice(self, new_price):
        self.price = new_price

    def getSpec(self):
        return self.spec

class InstrumentSpec(ABC):
    def __init__(self, builder, model, typeG, backWood, topWood):
        self.builder = builder
        self.model = model
        self.typeG = typeG
        self.backWood = backWood
        self.topWood = topWood

    def getBuilder(self):
        return self.builder

    def getModel(self):
        return self.model

    def getTypeG(self):
        return self.typeG

    def getBackWood(self):
        return self.backWood

    def getTopWood(self):
        return self.topWood

    @abstractmethod
    def matches(self, otherSpec):
        pass

class GuitarSpec(InstrumentSpec):
    def __init__(self, builder, model, typeG, backWood, topWood, numStrings):
        super().__init__(builder, model, typeG, backWood, topWood)
        self.numStrings = numStrings

    def getNumStrings(self):
        return self.numStrings

    def matches(self, otherSpec):
        if not isinstance(otherSpec, GuitarSpec):
            return False
        if self.builder != otherSpec.getBuilder():
            return False
        if self.model and self.model.lower() != otherSpec.getModel().lower():
            return False
        if self.typeG != otherSpec.getTypeG():
            return False
        if self.backWood != otherSpec.getBackWood():
            return False
        if self.topWood != otherSpec.getTopWood():
            return False
        if self.numStrings != otherSpec.getNumStrings():
            return False
        return True

class Guitar(Instrument):
    def __init__(self, serialNumber, price, spec):
        super().__init__(serialNumber, price, spec)

class MandolinSpec(InstrumentSpec):
    def __init__(self, builder, model, typeG, backWood, topWood, style):
        super().__init__(builder, model, typeG, backWood, topWood)
        self.style = style

    def getStyle(self):
        return self.style

    def matches(self, otherSpec):
        if not isinstance(otherSpec, MandolinSpec):
            return False
        if self.builder != otherSpec.getBuilder():
            return False
        if self.model and self.model.lower() != otherSpec.getModel().lower():
            return False
        if self.typeG != otherSpec.getTypeG():
            return False
        if self.backWood != otherSpec.getBackWood():
            return False
        if self.topWood != otherSpec.getTopWood():
            return False
        if self.style != otherSpec.getStyle():
            return False
        return True

class Mandolin(Instrument):
    def __init__(self, serialNumber, price, spec):
        super().__init__(serialNumber, price, spec)

class Inventory:
    def __init__(self):
        self.instruments = []

    def addInstrument(self, instrument):
        self.instruments.append(instrument)

    def getInstrument(self, serialNumber):
        for instrument in self.instruments:
            if instrument.getSerialNumber() == serialNumber:
                return instrument
        return None

    def search(self, searchSpec):
        matchingInstruments = []
        for instrument in self.instruments:
            if instrument.getSpec().matches(searchSpec):
                matchingInstruments.append(instrument)
        return matchingInstruments

# Testando o Sistema
def initializeInventory(inventory):
    guitarSpec1 = GuitarSpec(Builder.FENDER, "stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    inventory.addInstrument(Guitar("V95693", 1499.95, guitarSpec1))
    inventory.addInstrument(Guitar("V99999", 1599.95, guitarSpec1))

    mandolinSpec1 = MandolinSpec(Builder.GIBSON, "F-5G", TypeG.ACOUSTIC, Wood.MAPLE, Wood.MAPLE, "A-style")
    inventory.addInstrument(Mandolin("M12345", 1999.95, mandolinSpec1))
    inventory.addInstrument(Mandolin("M67890", 2999.95, mandolinSpec1))

def main():
    inventory = Inventory()
    initializeInventory(inventory)

    whatErinLikes = GuitarSpec(Builder.FENDER, "stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    matchingGuitars = inventory.search(whatErinLikes)

    if matchingGuitars:
        print("Erin, talvez você goste destas: ")
        for guitar in matchingGuitars:
            guitarSpec = guitar.getSpec()
            print(f"\nGuitarra: {guitar.getSerialNumber()} {guitarSpec.getBuilder().value} {guitarSpec.getModel()} {guitarSpec.getTypeG().value} guitar:\n{guitarSpec.getBackWood().value} na traseira e laterais,\n{guitarSpec.getTopWood().value} no tampo, com {guitarSpec.getNumStrings()} cordas\nEla pode ser sua por apenas US${guitar.getPrice():.2f}!")
    else:
        print("Desculpe Erin, não temos nada para você")

if __name__ == '__main__':
    main()