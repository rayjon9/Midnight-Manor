"""main.py

The main game loop.
"""
# By convention, import statements go at the top of the file

import game


if __name__ == "__main__":
    mud = game.Game()
    mud.welcome()
    player = data.create_player()
    mud.add_player(player)
    while not mud.is_gameover():
        game.show_room_desc()
        game.show_player_options()
        choice = game.get_player_option() 
        mud.execute(choice)
    if mud.is_gameover():
        result = game.win_or_lose()
    game.epilogue(result)
    
