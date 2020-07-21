
class Weapon:
    def __init__(self):
        raise NotImplementedError ("Dont create new weapon classes")
    def __str__(self):
        return self.name


class Dagger(Weapon):
    def __init__(self):
        self.name = 'Rusty Dagger'
        self.damage = 10
        self.des = 'a Rusty Dagger that you found when you woke up'
        self.value = 25
    

class Baton(Weapon):
    def __init__(self):
        self.name = 'Steel Baton'
        self.damage = 15
        self.des = 'Used Bloody steel baton'
        self.value = 50

class Sword(Weapon):
    def __init__(self):
        self.name = 'Anciet looking sword'
        self.damage = 25 
        self.des = 'This sword looks legendary... some anciet carving is on it.. interesting'
        self.value = 100

class Consume:
    def __init__(self):
        raise NotImplementedError ("Dont create Raw consumable classes")
    def __str__(self):
        return self.name

class Bread(Consume):
    def __init__(self):
        self.name = 'Crusty Bread'
        self.heal_value = 10
        self.value = 20

class HealthPotion(Consume):
    def __init__(self):
        self.name = 'Healing Potion'
        self.heal_value = 50
        self.value = 100




