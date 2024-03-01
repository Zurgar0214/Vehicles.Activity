from Models.Entities.Racer import Racer
from Models.Entities.Racing import Racing
from Service.Loader import Loader


if __name__ == "__main__":
    loader = Loader()
    vehicles = loader.load_data()
    print("Bienvenido a la carrera \nElige tu vehículo de la siguiente lista: \n")
    index : int = 1
    for vehicle in vehicles:
        print(f"{index}- {vehicle}")
        index += 1
    select : int =  int(input("Escribe tu elección: "))
    print("Veiculo seleccionado: " +vehicles[select-1])
    racer = Racer(vehicles[select-1],  input("Escribe tu nombre: "))
    racer.ChooseCar()
    select =  int(input("Cuántas vueltas quieres correr??: "))
    racing = Racing(select, "Copa Pistón")
    racing.add_player(racer)