import pygame


class Item:

    def __init__(self, position):
        self.position = pygame.Vector2(position)
        self.speed = 100

    def update(self, dt):
        self.position.x += self.speed * dt


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
