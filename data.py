def mud.welcome():
    """Displays the welcome screen when the player starts the game."""
    print("welcome")

def game.showroomdesc():
    """Displays the screen when the player enters the foyer."""
    print(f"{room} ({level})")
    print(f"{room desc}")
    print(f"{choices}") 
    def mud.get_options():
        """Takes the player's input and returns the corresponding action."""
        