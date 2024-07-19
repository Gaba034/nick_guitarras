#Classe Guitar
class Guitar:
    def __init__(self, serial_number, price, builder, model, typeg, back_wood, top_wood):
        self.serial_number = serial_number
        self.price = price
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.back_wood = back_wood
        self.top_wood = top_wood

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def get_builder(self):
        return self.builder

    def get_typeg(self):
        return self.typeg

    def get_model(self):
        return self.model

    def get_back_wood(self):
        return self.back_wood

    def get_top_wood(self):
        return self.top_wood
