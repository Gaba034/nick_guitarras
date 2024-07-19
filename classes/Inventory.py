from .Guitar import Guitar

class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, serial_number, price, builder, model, typeg, back_wood, top_wood):
        guitar = Guitar(serial_number, price, builder, model, typeg, back_wood, top_wood)
        self.guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self.guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None

    def search_guitar(self, search_guitar):
        for guitar in self.guitars:
            # Parece que nada mudou, mas com "Enums", não precisamos nos preocupar com essas comparações 
            # sendo prejudicadas por erros ortográficos ou problemas de maiúscula/minúscula
            if search_guitar.get_builder() != guitar.get_builder():
                continue
            
            # A única propriedade com a qual precisamos nos preocupar é o "model", já que ainda é uma String
            model = search_guitar.get_model().lower()
            if model and model != "" and model != guitar.get_model().lower():
                continue
            
            # Parece que nada mudou, mas com "Enums", não precisamos nos preocupar com essas comparações 
            # sendo prejudicadas por erros ortográficos ou problemas de maiúscula/minúscula
            if search_guitar.get_typeg() != guitar.get_typeg():
                continue
            if search_guitar.get_back_wood() != guitar.get_back_wood():
                continue
            if search_guitar.get_top_wood() != guitar.get_top_wood():
                continue
            return guitar
        return None
    
