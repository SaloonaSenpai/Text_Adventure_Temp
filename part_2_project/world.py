import random, enemies , npc

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")
    
    def modify_player(self, player):
        pass 


class StartTile(MapTile):
    def intro_text(self):
        return """
                you find your self in a dark room with an annoying flickering light...
                you make out 4 paths, your eyes caught an object.. 
                you held a bloody baton..

                "This might be handful" you said as you stood there glazing on the empty dark paths....
        """

class EnemyTile(MapTile):
    def __init__(self, x , y):
        r = random.random()
        if r < 0.50 :
            self.enemy = enemies.Slime()
            self.alive_text = "A slime makes it way toward you, WATCH OUT ITS POISONOUS"
            self.dead_text = "The slime melted as it dies.. no trace of its existice left"
        elif r < 0.85:
            self.enemy = enemies.Zombie()
            self.alive_text = "You hear a groan from behind you.. you lock your eyes with the undead.. it notices you and starts running toward you"
            self.dead_text = "What once was a corpse is now a corpse again?"
        elif r < 0.90:
            self.enemy = enemies.SlimeColony()
            self.alive_text= "One Slime.. Two Slime.. Three Slime.. you lose count as the a large Colony of Slimes marches it was toward you"
            self.dead_text = "Finally you killed the whole colony that took long huh?"
        else:
            self.enemy = enemies.Frankenstein()
            self.alive_text = "Frankenstein's monster stood in front of you, you looked at the large monster.. You started praying as you held your weapon tightly"
            self.dead_text = "Frankenstein must be mad at you now.. sucks to be you"

        super().__init__(x,y)

    def intro_text(self):
        if self.enemy.is_alive():
            return self.alive_text
        else:
            return self.dead_text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp -= self.enemy.damage
            print("Enemy dealt {} damage, You have {} HP left!".format(self.enemy.damage, player.hp ))


class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True 

    def intro_text(self):
        return """
                You see a room with a white door.. a bloody white door you smiled as you read the exit logo
                you opened the door to meet the full moon shinning on you 

                You have escaped.. enjoy while it lasts  
        """

class FindGoldTile(MapTile):
    def __init__(self,x,y):
        self.gold = random.randint(1,50)
        self.gold_claim = False
        super().__init__(x,y)

    def modify_player(self, player):
        if not self.gold_claimL:
            self.gold_claim = True
            player.gold += self.gold
            print("+{} gold has been added".format(self.gold))
    def intro_text(self):
        if self.gold_claimed:
            return """
            Just another dark room..
            you must continue looking for the exit
            """
        else:
            return """
            someone left some gold. You picked it up 
            """


class TradeTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x,y)
    #we need to make a trade function that allows the player to buy the items 
    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item to buy or press Q to quit/exit: ").lower()
            if user_input == 'q':
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory(choice - 1)
                    self.swap(seller,buyer,to_swap)
                except ValueError:
                    print("Invalid choice")
    
    #this would remove/ add item and deals with the gold math 
    def swap(self, buyer, seller):
        if item.value > buyer.gold:
            return print("Its Too Expesnive")
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + buyer.gold
        buyer.gold = buyer.gold - item.value
        print("Trade Complete")

    #the thing is a buyer can be the NPC or the player/ player can buy adn sell 
    def check_if_trade(self, player):
        while True:
            print("Would you like to buy, sell, or quit")
            user_input = input()
            if user_input in ['quit', 'Quit']:
                return 
            elif user_input in ['buy', 'Buy']:
                print('Heres are the avalible items to buy: ')
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['Sell', 'sell']:
                print('Here is what is avalible to sell: ')
                self.trade(buyer=self.trader , seller=player)
            else:
                print("inavlid")
            
    def intro_text(self):
        return """
        You find you self looking at an alien creature like an anglerfish with ligh bulb attacked to his head
        you notice it smirking at you 
        "Wanna trade?" the creature asked with a grin

        """


world_dsl = """
|EN|EN|VT|EN|EN|
|FG|EN|  |EN|FG|
|TT|  |  |FG|TT|
|EN|FG|ST|  |EN|
|EN|  |EN|  |FG|  
"""
#count on number of start tiles, victory tiles a
def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

            
    return True

#the dictonary of the map so we can use the VT , since we have the command above to read world_dls
tile_type_dict = {"VT" : VictoryTile ,
                   "EN" :EnemyTile ,
                   "ST": StartTile,
                   "TT": TradeTile,
                   "FG": FindGoldTile,
                   "  " : None}


world_map = []

#since we changed the locatino of the start the game wouldnt work so now we have
#to make it calm down that its okay 

start_tile_location = None

#dont fully understand this 
def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")


    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines): #using y for the girds
        row = []
        dsl_cells = dsl_row.split("|") #split the lines into abberviations
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):   #using x for the grid 
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x , y 
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)

#go back the loops when they use the J


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
