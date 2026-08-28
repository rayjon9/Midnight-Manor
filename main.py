"""main.py

The main game loop.
"""
# By convention, import statements go at the top of the file

import game
import data

if __name__ == "__main__":
    mud = game.Game()
    mud.welcome()
    player = data.create_player()
    mud.add_player(player)
    while not mud.is_gameover():
        game.show_room()
        game.show_player_choice()
        choice = game.get_player_choice() 
        mud.execute(choice)
        data.display(mud.status())
    if mud.is_gameover():
        result = game.win()
    game.epilogue(result)
    
