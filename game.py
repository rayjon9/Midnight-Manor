import random
class Game:
    def __init__(self):
        self.players = []
    
    def add_player(self, player):
        self.players.append(player)
        player.spawn(current_room.spawn_x, current_room.spawn_y)
        
    def execute():
        pass
    def show_room(current_room):
        print(current_room)
    def show_player_choices():
        pass
    def monster_encounter():
        encounter = random.randint(3,7)
        
    def is_gameover():
        pass

class Room:
    def __init__(self, layout):
        self.layout = layout
        self.next_room = None
    def get_layout(self):
        for row in self.layout:
            print(row)
    def set_starting_point(self, x, y):
        self.spawn_x = x
        self.spawn_y = y
    def search_grid(self, x, y):
        if x < 0 or x > 7 or y < 0 or y > 7:
             return "M"
        return self.layout[y][x]
    def change(self):
        global current_room
        current_room = self.next_room
        player.x, player.y = current_room.spawn_x, current_room.spawn_y
    
class Player:
    def __init__(self):
        self.x = None
        self.y = None
        self.inv = [None, None, None, None, None]
        self.hp = 25
        self.atk = 2
    def spawn(self, x, y):
        self.x = x
        self.y = y
    def get_coords(self):
        print(self.x, self.y)
    def add_item(self, item):
        for i in range(len(self.inv)):
            if self.inv[i] == None:
                self.inv[i] = item
            break
    def get_inv(self):
        print(f"Inventory ({len(self.inv)}):")
        for item in self.inv:
            print(item)
    def choice_move(self):
        global current_room
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
            self.get_inv()
        else:
            print("Choice does not exist!")
    def choice_inv(self):
        self.get_inv()
        dcs = input(f"1 - {self.inv[0]}, 2 - {self.inv[1]}, 3 - {self.inv[2]}, 4 - {self.inv[3]}, 5 - {self.inv[4]}")

    def choice_fight(self):
        global monster
        print(f"Monster Hp = {monster.hp}, Your HP = {self.hp}")
        dcs = input("1 - Attack, E - Open Inventory")
        if dcs == "1":
            monster.hp -= self.atk
            print(f"You attacked the {monster.name} for {self.atk} damage!")
        if dcs.upper() == "E":
            self.choice_inv()

class Monster:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk
    def get_stats(self):
        print(self.name, self.hp, self.atk)

def win_or_lose():
    pass

def epilogue(result):
    pass


foyer = Room([["M","M","M","M","M","M","M","M"],
        ["M","M","M","M","M","M","M","M"],
        ["M","M","M","M","M","M","M","M"],
        [".",".",".",".",".",".",".","."],
        ["X",".",".",".",".",".",".","E"],
        [".",".",".",".",".",".",".","."],
        ["M","M","M","M","M","M","M","M"],
        ["M","M","M","M","M","M","M","M"]])
foyer.set_starting_point(0, 4)
ballroom = Room([["M","M","M","E","E","M","M","M"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        ["M","M",".","M","M",".","M","M"],
        ["M","M",".","M","M",".","M","M"],
        ["X",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        ["M","M","M","M","M","M","M","M"]])
ballroom.set_starting_point(0, 5)
foyer.next_room = ballroom
current_room = foyer

player = Player()
player.spawn(current_room.spawn_x, current_room.spawn_y)
player.add_item("Rusty Dagger")
monster = Monster("Phantom", 15, 5)
ph_encounter = random.randint(3,7)
#player.get_coords()

game = True
while game:
    if current_room == ballroom:
        ph_encounter -= 1
    while ph_encounter == 0:
        print("YOU GOT IN A FIGHT")
        print("YOU GOT IN A FIGHT")
        player.choice_fight()
        if monster.hp <= 0:
            ph_encounter = 99999999999
            print("fight over")
    else:
        current_room.get_layout()
        player.choice_move()
