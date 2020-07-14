class weapon:
    def __init__(self):
        raise NotImplementedError("Do not create Raw Weapon Object")

    def __str__(self):
        return self.name


class Rock(weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A flat-sized rock"
        self.damage = 5


class Dagger(weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A Rusty dagger, looks more dangerous than the rock" 
        self.damage = 10


class RustySword(weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "This sword looks old but still still can manage"
        self.damage = 20
