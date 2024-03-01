from Models.Entities.Vehicle import Vehicle


class Motorcycle(Vehicle):
    '''
    Subclase que hereda de vehículo
    '''
    def __init__(self, maximun_speed: int, gasoline_capacity: int, type: str):
        super().__init__(maximun_speed, gasoline_capacity)
        self.type = type
