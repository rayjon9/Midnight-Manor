class Game:
    def welcome():
        pass
    def add_player(player):
        player = Player()
        player.spawn(current_room.spawn_x, current_room.spawn_y)
        pass
    def execute():
        pass
    def show_room(current_room):
        print(current_room)
    def show_player_choices():
        pass

class Room:
    def __init__(self, layout):
        self.layout = layout
        self.next_room = None
    def get_layout(self):
        print(self.layout)
    def set_starting_point(self, x, y):
        self.spawn_x = x
        self.spawn_y = y
    def search_grid(self, x, y):
        if x < 0 or x > 7 or y < 0 or y > 7:
             return "M"
        return self.layout[y][x]
    def change(self):
        current_room = self.next_room
        print(current_room)
    
class Player:
    def __init__(self):
        self.x = None
        self.y = None
        self.inv = []
        self.hp = 25
    def spawn(self, x, y):
        self.x = x
        self.y = y
    def get_coords(self):
        print(self.x, self.y)
    def append_inv(self, item):
        self.inv.append(item)
    def get_inv(self):
        for item in self.inv:
            print(item)
    def choice(self):
        dcs = input("WASD - Move, E - Open Inventory")
        if dcs.upper() == "W":
            if current_room.search_grid(self.x, self.y - 1) == ".":
                current_room.layout[self.y][self.x] = "."
                self.y -= 1
                current_room.layout[self.y][self.x] = "X"
            elif current_room.search_grid(self.x, self.y - 1) == "E":
                current_room.change()
            else:
                print("Move not available!")
        elif dcs.upper() == "A":
            if current_room.search_grid(self.x - 1, self.y) == ".":
                current_room.layout[self.y][self.x] = "."
                self.x -= 1
                current_room.layout[self.y][self.x] = "X"
            elif current_room.search_grid(self.x - 1, self.y) == "E":
                current_room.change()
            else:
                print("Move not available!")
        elif dcs.upper() == "S":
            if current_room.search_grid(self.x, self.y + 1) == ".":
                current_room.layout[self.y][self.x] = "."
                self.y += 1
                current_room.layout[self.y][self.x] = "X"
            elif current_room.search_grid(self.x, self.y + 1) == "E":
                current_room.change()
            else:
                print("Move not available!")
        elif dcs.upper() == "D":
            if current_room.search_grid(self.x + 1, self.y) == ".":
                current_room.layout[self.y][self.x] = "."
                self.x += 1
                current_room.layout[self.y][self.x] = "X"
            elif current_room.search_grid(self.x + 1, self.y) == "E":
                current_room.change()
            else:
                print("Move not available!")
        elif dcs.upper() == "E":
            get_inv()
        else:
            print("Choice does not exist!")

foyer = Room([["M","M","M","M","M","M","M","M"],
        ["M","M","M","M","M","M","M","M"],
        ["M","M","M","M","M","M","M","M"],
        [".",".",".",".",".",".",".","."],
        ["X",".",".",".",".",".",".","E"],
        [".",".",".",".",".",".",".","."],
        ["M","M","M","M","M","M","M","M"],
        ["M","M","M","M","M","M","M","M"]])
foyer.set_starting_point(0, 4)
living = Room([["M","M","M","E","E","M","M","M"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        ["X",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        ["M","M","M","M","M","M","M","M"]])
living.set_starting_point(0, 4)
foyer.next_room = living
current_room = foyer

player = Player()
player.spawn(current_room.spawn_x, current_room.spawn_y)
#player.get_coords()

while game:
    current_room.get_layout()
    player.choice()
    