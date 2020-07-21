
class Enemy:
    def __init__(self):
        raise NotImplementedError ("Dont Create Enemy class")
    def __str__(self):
        return self.name
    def is_alive(self):
        return self.hp > 0 


class Zombie(Enemy):
    def __init__(self):
        self.name = 'Zombie'
        self.hp = 50
        self.damage = 10

class Slime(Enemy):
    def __init__(self):
        self.name = 'Red Slime'
        self.hp = 10
        self.damage = 2

class SlimeColony(Enemy):
    def __init__(self):
        self.name = 'Colony of Slimes'
        self.hp = 100
        self.damage = 5

class Frankenstein(Enemy):
    def __init__(self):
        self.name = "Frankenstein's Monster"
        self.hp = 80
        self.damage = 15
