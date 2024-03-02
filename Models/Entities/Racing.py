from random import randint
from Models.Entities.Car import Car
from Models.Entities.Racer import Racer
class Racing:
    '''
    Clase que representa la carrera que se lleva a cabo.
    '''
    def __init__(self, num_laps: int, name :str):
        self.num_laps = num_laps
        self.players: Racer = []
        self.name = name

    def add_player(self, player: Racer):
        self.players.append(player)

    def add_players(self, players: list[Racer]):
        self.players.extend(players)

    def calculateScore(self, speedUp: bool):
        for player in self.players:
            action: int = randint(1,2)
            if player.isMainPlayer:
                player.Action(speedUp)
            elif action is 1:
                player.Action(True)
            else:
                player.Action(False)
