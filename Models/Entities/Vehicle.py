class Vehicle:
    '''Clase padre, que usaremos como referencia para las demás subclases'''
    def __init__(self, maximun_speed: int, gasoline_capacity: int):
        
        self.maximun_speed = maximun_speed
        self.gasoline_capacity = gasoline_capacity
        self.current_speed = 0
    
    def speedUp(self, increase: int) -> int:
        '''
        Método para acelerar
        @increase -> cantidad que acelerará
        '''
        self.current_speed = min(self.current_speed + increase, self.maximun_speed)
        return self.current_speed
    
    def brake(self, decrease: int) -> int:
        '''
        Método para frenar
        @decrease -> cantidad que disminuirá la velocidad del vehículo
        '''
        self.current_speed = max(self.current_speed + decrease, 0)
        return self.current_speed