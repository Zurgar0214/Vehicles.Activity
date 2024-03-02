from random import randint
from Models.Entities.Racer import Racer
from Models.Entities.Racing import Racing
from Models.Entities.Vehicle import Vehicle
from Service.Loader import Loader

def setCarsToRacers(carsList: list[Vehicle], racersList: list[Racer]) -> list[Racer]:
    for racer in racersList:
        racer.car = carsList[randint(0, len(carsList)-1)]
    return racersList

def startRace():
    loader = Loader()
    vehicles, racers = loader.load_data()
    print("Bienvenido a la carrera \nElige tu vehículo de la siguiente lista: \n")
    index : int = 1
    for vehicle in vehicles:
        print(f"{index}- {vehicle}")
        index += 1
    index = 1
    select : int =  int(input("Escribe tu elección: "))
    print(f"Vehículo seleccionado {vehicles[select-1]}")
    racer = Racer(vehicles[select-1],  input("Escribe tu nombre: "))
    racer.ChooseCar()
    racers = setCarsToRacers(vehicles, racers)
    select =  int(input("¿Cuántas vueltas quieres correr?: "))
    racing:Racing = Racing(select, "Copa Pistón")
    racing.add_player(racer)
    racing.add_players(racers)

    racing = RunRace(racing)
    print("clasificación final: ")
    for racer in sorted(racing.players, key = lambda racer : racer.score, reverse=True):
        print(f"{index}. Nombre: {racer.nickName}, Puntuación: {racer.score}")
        index += 1
    print("-"*70)


def RunRace(race: Racing) -> Racing:
    if race.num_laps == 0:
        return race
    else:
        select:int = int(input("¿Qué desea hacer para esta vuelta? (1 -> acelerar) (2 -> frenar): "))
        race.calculateScore(select is 1)
        race.num_laps = race.num_laps - 1
        race = RunRace(race)
    return race

if __name__ == "__main__":
    startRace()