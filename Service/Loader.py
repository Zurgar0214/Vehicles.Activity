import os
import json
from Models.Entities.Vehicle import Vehicle
from Models.Entities.Motorcycle import Motorcycle
from Models.Entities.Car import Car
from Models.Enums.MotorcycleType import MotorcycleType

class Loader:
    def __init__(self, data_folder='Data'):
        self.data_folder = data_folder

    def load_json(self, file_name):
        file_path = os.path.join(self.data_folder, file_name)
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    def load_data(self, json_file='vehicles_data.json') -> list[Vehicle]:
        data = self.load_json(json_file)
        # Crear instancias de Motorcycle
        motorcycles = [Motorcycle(**m) for m in data["motorcycles"]]
        for motorcycle in motorcycles:
            motorcycle.type = MotorcycleType[motorcycle.type]

        # Crear instancias de Car
        cars = [Car(**c) for c in data["cars"]]

        vehicles = cars
        vehicles += motorcycles

        return vehicles