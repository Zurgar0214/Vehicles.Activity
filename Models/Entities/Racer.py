from random import randint, randrange
from Models.Entities.Car import Car
from Models.Entities.Vehicle import Vehicle


class Racer:
    def __init__(self, car:Vehicle, nickName :str ):
        self.car = car
        self.nickName = nickName
        self.score : int = 1
        self.isMainPlayer: bool = False
        
    def RandomTime(self):
        self.score += randint(self.car.current_speed, self.car.current_speed +100)
    
    def Action(self, action: bool):
        if action:
            self.car.speedUp(self.score)
            self.RandomTime()
        else :
            self.car.brake(self.score)
            self.RandomTime()

    def ChooseCar(self):
        self.isMainPlayer = True
