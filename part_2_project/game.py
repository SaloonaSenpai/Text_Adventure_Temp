#incase the project fail this is basically the second part 
# includes working with dictonaries and removing the bugs that are annoying 


from player import Player
from collections import OrderedDict
import world


def play():
    print("Escape from Cave Terror!")
    world.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print("You Died!")


def choose_action(room, player):
    action = None
    while not action:
        available_action = get_available_actions(room, player)
        action_input = input('Action: ')
        action = available_action.get(action_input)
        if action:
            action()
        else:
            print("Invalid action")



#<<<<<<<<<<<<<<<<<<<<<<<Author_Note>>>>>>>>>>>>>>>>>>>>>>>>>>>#
'''
This function will tell us which action is avalible, if player health is less than 100
they can heal.. if enemy is present and they are alive player can attack 
actions including the movement and inventory 
also added dictonary that would give us the hotkeys for the game PLUS the usage

'''
#<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>#

def get_available_actions(room, player):
    actions = OrderedDict()
    print('Choose an Action: ')
    if player.inventory:
        action_adder(actions, 'inv', player.print_inventory, 'Print inventory')
    if isinstance(room, world.TradeTile):
        action_adder(actions, 'trade', player.trade,'to trade')
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'attack', player.attack, "Attack")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'north', player.move_north, 'Go north')
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 'south', player.move_south, 'Go South')
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'west', player.move_west, 'Go West')
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'east', player.move_east, 'Go East')
    if player.hp < 100:
        action_adder(actions, 'heal', player.heal, 'To Heal')

    return actions

def action_adder(action_dict, hotkey, action,name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print('{} : {}'.format(hotkey, name))




play()
