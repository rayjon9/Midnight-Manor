from game import Player, Room

def create_player():
    """Creates a new player object."""
    name = input("Enter your character's name: ")
    return Player(name)

def create_room():
    """Creates a new room object."""
    layout = room.txt
    with open("room.txt", "r") as f:
        layout = []
        for line in f:
            layout.append(line.strip().split())
    room = Room()
    room.set_layout(layout)
    return room
def welcome():
    """Displays a welcome message to the player."""
    print("Welcome to the MUD game!")
    print("You are about to embark on an adventure.")
    print("Good luck!")

def display(status: dict):
    """Displays the current game status."""
    print("============================================================")
    print(status["room_name"])
    print("============================================================")
    print(status["item_description"])
    print(status["enemy_description"])
    print("------------------------------------------------------------")
    for i, option in enumerate(status["options"], start=1):
        print(f"{i} - {option}")
    print("------------------------------------------------------------")

def epilogue(result):
    """Displays an epilogue message to the player."""
    if result:
        print("============================================================")
        print("DILAPIDATED ATTIC")
        print("============================================================")
        print("You strike the Wraith with your blade. \nAs the blade pierces its ghastly body, \nthe Wraith vanishes into thin air, \nnever to be seen again.")
        print("****************************************")
        print("*   YOU HAVE SLAIN THE WRAITH.         *")
        print("*   THE MANOR HAS BEEN CLEANSED.       *")
        print(" ****************************************")
        print("You have won the game. Congratulations!")
        print("Thank you for playing!")
    else:
        print("============================================================")
        print("DILAPIDATED ATTIC")
        print("============================================================")
        print("The Wraith strikes you with its ghastly blade. \nYou feel your life force draining away as the Wraith's attack pierces your body.")
        print("****************************************")
        print("*   YOU HAVE BEEN SLAIN BY THE WRAITH. *")
        print("*   THE MANOR REMAINS HAUNTED.         *")
        print(" ****************************************")
        print("You have lost the game. Better luck next time!")
        print("Thank you for playing!")