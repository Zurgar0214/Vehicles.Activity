from typing import List, Tuple
import os
import json
from Models.Entities.Racer import Racer
from Models.Entities.Vehicle import Vehicle
from Models.Entities.Motorcycle import Motorcycle
from Models.Entities.Car import Car

class Loader:
    def __init__(self, data_folder='Data'):
        self.data_folder = data_folder

    def load_json(self, file_name):
        file_path = os.path.join(self.data_folder, file_name)
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    def load_data(self, json_file='vehicles_data.json') -> Tuple[List[Vehicle], List[Racer]]:
        data = self.load_json(json_file)
        # Crear instancias de Motorcycle
        motorcycles = [Motorcycle(**moto) for moto in data["motorcycles"]]
        # Crear instancias de Car
        cars = [Car(**car) for car in data["cars"]]
        # Crear instancias de Racers
        racers = [Racer(**racer) for racer in data["racers"]]        
        vehicles = cars
        vehicles += motorcycles

        return vehicles, racers