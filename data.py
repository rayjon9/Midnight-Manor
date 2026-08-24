from game import Player

def create_player():
    """Creates a new player object."""
    name = input("Enter your character's name: ")
    return Player(name)

def create_room():
    """Creates a new room object."""
    layout = []
    for i in range(8):
        row = input(f"Enter row {i+1} of the room layout (use '.' for empty space and 'M' for walls): ")
        layout.append(list(row))
    room = Room()
    room.set_layout(layout)
    return room
    
def display(status):
    """Displays the current game status."""
    print(f"Current Status: {status}")

