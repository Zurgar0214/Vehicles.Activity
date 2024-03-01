from Models.Entities.Vehicle import Vehicle


class Car(Vehicle):
    '''
    Subclase que heredará de vehículo
    '''
    def __init__(self, maximun_speed: int, gasoline_capacity: int, doors_quantity: int):
        super().__init__(maximun_speed, gasoline_capacity)
        self.doors_quantity = doors_quantity
    