class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Machine:
    def __init__(self, name, position, direction):
        self.name = name
        self.position = position
        self.direction = direction


class Conveyor:
    def __init__(self, position, direction, speed=100,  capacity=5):
        self.position = position
        self.direction = direction
        self.speed = speed
        self.capacity = capacity
        self.items = []

    def get_pos(self):
        pass

    def get_direction(self):
        pass
