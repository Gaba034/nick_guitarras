class Logger():

    def __init__(self, value, message):
        self.value = value
        self.message = message

    def log(self):
        if self.value is not None:
            try:
                print(self.message)
            except Exception:
                print(f"Error in logging: {KeyError}")
        elif self.value is None:
            print("Não encontramos nada no estoque, sinto muito.")
