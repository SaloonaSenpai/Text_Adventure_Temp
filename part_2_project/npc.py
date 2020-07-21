import items

class NonPlayerCharacter:
    def __init__(self):
        raise NotImplementedError("dont create raw NPCS")
    def __str__(self):
        return self.name()
    

class Trader(NonPlayerCharacter):
    def __init__(self):
        self.name = 'the Trader'
        self.gold = 100
        self.inventory = [items.Bread(), items.Bread(),
                        items.HealthPotion(), items.HealthPotion(),
                         items.Sword(),]
