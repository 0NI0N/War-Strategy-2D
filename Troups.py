import pygame


class Swordsman(pygame.sprite.Sprite):
    def __init__(self):
        self.velocity = 50
        self.health = 60
        self.damage = 60
        self.moral = 75
        self.range = 1


class Bowman(pygame.sprite.Sprite):
    def __init__(self):
        self.velocity = 65
        self.health = 20
        self.damage = 20
        self.bow_damage = 40
        self.damage = 20
        self.moral = 60
        self.range = 60



