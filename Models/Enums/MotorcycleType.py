import enum

class MotorcycleType(enum):
    SCOOTER = 1
    MAXISCOOTER = 2
    CHOPPER = 3
    SPORT = 4

MotorcycleType = enum('Type', ['SCOOTER', 'MAXISCOOTER', 'CHOPPER', 'SPORT'])