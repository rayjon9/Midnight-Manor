# class Game:
#     def welcome():

#     def add_player(player):

#     def show_room(room):
#         print(room)
#     def show_player_options():

class Room:
    def __init__(self):
        self.layout = []
    def set_layout(self, layout):
        self.layout = layout
    def get_layout(self):
        print(self.layout)
    def set_starting_point(self, x, y):
        self.spawn_x = x
        self.spawn_y = y
    def set_exit(self, x, y):
        self.exit_x = x
        self.exit_y = y
    def search_grid(self, x, y):
        return self.layout[y][x]
        
class Player:
    def __init__(self, x, y):
        self.x = None
        self.y = None
    def spawn(self, x, y):
        self.x = x
        self.y = y
    def query(self, tile):
        if tile = "M":
            break
        if tile = "."
    def get_coords(self):
        print(self.x, self.y)
    def choice(self):
        dcs = input("WASD - Move, E - Open Inventory")
        if dcs.upper() == "W":
            
            self.y += 1

foyer = Room()
foyer.set_layout([["M","M","M","M","M","M","M","M"],
        ["M","M","M","M","M","M","M","M"],
        ["M","M","M","M","M","M","M","M"],
        [".",".",".",".",".",".",".","."],
        ["X",".",".",".",".",".",".","E"],
        [".",".",".",".",".",".",".","."],
        ["M","M","M","M","M","M","M","M"],
        ["M","M","M","M","M","M","M","M"]])
foyer.get_layout()
foyer.set_starting_point(0, 4)
foyer.set_exit(7, 4)
current_room = foyer

player = Player(None,None)
player.spawn(current_room.spawn_x, current_room.spawn_y)
player.get_coords()

player.query(foyer.search_grid(player.get_coords()))
