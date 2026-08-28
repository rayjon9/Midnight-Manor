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

