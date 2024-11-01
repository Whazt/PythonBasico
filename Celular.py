class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    

class Samsung:
    def __init__(self, marca, modelo, camara, precio) :
        super().__init__(marca, modelo, camara)
        self.precio = precio