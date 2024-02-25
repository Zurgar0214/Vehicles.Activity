from Models.Entities.Vehicle import Vehicle
from Models.Enums.MotorcycleType import MotorcycleType


class Motorcycle(Vehicle):
    '''
    Subclase que hereda de vehículo
    '''
    def __init__(self, maximun_speed: int, gasoline_capacity: int, type: MotorcycleType):
        super().__init__(maximun_speed, gasoline_capacity)
        self.type = type
