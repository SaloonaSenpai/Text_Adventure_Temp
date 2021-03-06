import item

class Player:
    def __init__(self):
        self.inventory = [item.Rock(), item.Dagger(), 'Crusty bread', 'Gold(5)' ]
        self.hp = 100

    def print_inventory(self):
        print("Inventory: ")
        for item in self.inventory:
            print(">>" + str(item))
        best_weapon = self.most_powerful_weapon()    
        print("Your best weapon is your {}".format(best_weapon))


    def most_powerful_weapon (self):
        max_damage = 0 
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon
