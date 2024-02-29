class Racing:
    '''
    Clase que representa la carrera que se lleva a cabo.
    '''
    def __init__(self, num_vueltas: int, name :str):
        self.num_vueltas = num_vueltas
        self.cars = []

    def agregar_carro(self, carro):
        self.cars.append(carro)