import player


 #>>{control player's movement}<<#
def play():
    print("Escape from Cave Terror!")
    player = player.Player()
    while True:
        action_input = get_player_command()
        if action_input == 'n':
            print("Going North")
        elif action_input == 'e':
            print("Going East")
        elif action_input == 's':
            print("Going South")
        elif action_input == 'w':
            print("Going West")
        elif action_input in ["inventory"]:
           player.print_inventory()
        else:
            print('Invalid Action')


#>>{this will return the player's actions}<<#
def get_player_command():
    return input('Action: ').lower()


play()

