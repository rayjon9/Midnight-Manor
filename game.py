import random
import time

class Game:
    def __init__(self):
        self.is_not_over = True
        self.current_room = None
        self.room_multi = 0
        self.ph_encounter = 999999999
        self.player = None
    def load_rooms(self):
        self.foyer = Room([["M","M","M","M","M","M","M","M", "M"],
                ["M","M","M","M","M","M","M","M", "M"],
                ["M","M","M","M","M","M","M","M", "M"],
                [".",".",".",".",".",".","E","M","M"],
                ["X",".",".",".",".",".","E","M","M"],
                [".",".",".",".",".",".","E","M","M"],
                ["M","M","M","M","M","M","M","M", "M"],
                ["M","M","M","M","M","M","M","M", "M"],
                ["M","M","M","M","M","M","M","M", "M"]], "FOYER")
        self.foyer.set_starting_point(0, 4)
        self.ballroom = Room([["M","M","M","E","E","E","M","M","M"],
                [".",".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".",".","."],
                ["M","M",".","M","M","M",".","M","M"],
                ["M","M",".","M","M","M",".","M","M"],
                ["M","M",".","M","M","M",".","M","M"],
                ["X",".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".",".","."],
                ["M","M","M","M","M","M","M","M","M"]], "BALLROOM")
        self.foyer.next_room = self.ballroom
        self.ballroom.set_starting_point(0, 6)
        self.dining_room = Room([["M","M","M","E","E","E","M","M","M"],
                [".",".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".",".","."],
                [".",".","M","M","M","M","M",".","."],
                [".",".","M","M","M","M","M",".","."],
                [".",".","M","M","M","M","M",".","."],
                [".",".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".",".","."],
                ["M","M","M","M","X","M","M","M","M"]], "DINING ROOM")
        self.ballroom.next_room = self.dining_room
        self.dining_room.set_starting_point(4, 8)
        self.staircase_1 = Room([["M","M","M","M","M","M","M","M","M"],
                ["M","M","M","M","M","M","M","M","M"],
                ["M","M","M","M","M","M","M","M","M"],
                ["M","M","M",".",".",".","M","M","M"],
                ["M","M","M","X","M",".","M","M","M"],
                ["M","M","M","M","E",".","M","M","M"],
                ["M","M","M","M","M","M","M","M","M"],
                ["M","M","M","M","M","M","M","M","M"],
                ["M","M","M","M","M","M","M","M","M"]], "STAIRCASE")
        self.dining_room.next_room = self.staircase_1
        self.staircase_1.set_starting_point(3, 4)
        self.staircase_2 = Room([["M","M","M","M","M","M","M","M","M"],
                ["M","M","M","M","M","M","M","M","M"],
                ["M","M","M","M","M","M","M","M","M"],
                ["M","M","M",".",".",".","M","M","M"],
                ["M","M","M",".","M","E","M","M","M"],
                ["M","M","M",".","X","M","M","M","M"],
                ["M","M","M","M","M","M","M","M","M"],
                ["M","M","M","M","M","M","M","M","M"],
                ["M","M","M","M","M","M","M","M","M"]], "STAIRCASE")
        self.staircase_1.next_room = self.staircase_2
        self.staircase_2.set_starting_point(4, 5)
        self.dark_corridor = Room([["M","M","M","M","M","M","M","M","M"],
                ["M","M","M","M","M","M","M","M","M"],
                ["M","M","M","M","M","M","M","M","M"],
                [".",".",".",".",".",".",".",".","E"],
                ["X",".",".",".",".",".",".",".","E"],
                [".",".",".",".",".",".",".",".","E"],
                ["M","M","M","M","M","M","M","M","M"],
                ["M","M","M","M","M","M","M","M","M"],
                ["M","M","M","M","M","M","M","M","M"]], "DARK CORRIDOR")
        self.staircase_2.next_room = self.dark_corridor
        self.dark_corridor.set_starting_point(0, 4)
        self.attic = Room([["M","M","M","M","M","M","M","M","M"],
                [".",".",".","M","M","M",".",".","."],
                [".",".","M","M","M",".",".","M","."],
                [".",".",".","M",".",".",".",".","."],
                ["X",".",".",".",".",".",".",".","E"],
                [".","M",".",".",".",".",".",".","."],
                [".","M",".",".","M","M",".","M","."],
                [".",".",".",".","M","M",".",".","."],
                ["M","M","M","M","M","M","M","M","M"]], "ATTIC")
        self.dark_corridor.next_room = self.attic
        self.attic.set_starting_point(0, 4)
        self.current_room = self.foyer
    def add_player(self):
        self.player = Player()
        self.player.spawn(self.current_room.spawn_x, self.current_room.spawn_y)
    def add_monster(self, monster):
        self.monster = monster
    # def show_player_choices():
    #     pass
    # def monster_encounter():
    #     pass

class Room:
    def __init__(self, layout, name):
        self.layout = layout
        self.next_room = None
        self.name = name
    def get_layout(self):
        print("===============================")
        print(self.name)
        print("===============================")
        for row in self.layout:
            print(row)
    def set_starting_point(self, x, y):
        self.spawn_x = x
        self.spawn_y = y
    def search_grid(self, x, y):
        if x < 0 or x > 8 or y < 0 or y > 8:
             return "M"
        return self.layout[y][x]
    def change(self):
        game.current_room = self.next_room
        game.room_multi += 1
        game.player.x, game.player.y = game.current_room.spawn_x, game.current_room.spawn_y
        if game.current_room == game.attic:
            time.sleep(1)
            print("You climb up the rusty ladder into the attic.")
            time.sleep(1)
            print("The dust suffocates you as you enter it.")
            print("")
        if game.current_room != game.dark_corridor:
            game.ph_encounter = random.randint(4, 7)
            game.add_monster(Monster("Phantom", 7 + 3 * game.room_multi, -1 + 3 * game.room_multi))

class Player:
    def __init__(self):
        self.x = None
        self.y = None
        self.inv = [None, None, None, None, None]
        self.hp = 25
        self.max_hp = 25
        self.atk = 2
    def spawn(self, x, y):
        self.x = x
        self.y = y
    def get_coords(self):
        print(self.x, self.y)
    def add_item(self, item):
        for i in range(len(self.inv)):
            if self.inv[i] is None:
                self.inv[i] = item
                break
    def get_inv(self):
        print(f"Inventory ({len(self.inv)}):")
        for item in self.inv:
            print(item)
    def choice_move(self):
        game.ph_encounter -= 1
        dcs = input("WASD - Move, E - Open Inventory  ")
        if dcs.upper() == "W":
            if game.current_room.search_grid(self.x, self.y - 1) == ".":
                game.current_room.layout[self.y][self.x] = "."
                self.y -= 1
                game.current_room.layout[self.y][self.x] = "X"
            elif game.current_room.search_grid(self.x, self.y - 1) == "E":
                game.current_room.change()
            else:
                print("Move not available!")
        elif dcs.upper() == "A":
            if game.current_room.search_grid(self.x - 1, self.y) == ".":
                game.current_room.layout[self.y][self.x] = "."
                self.x -= 1
                game.current_room.layout[self.y][self.x] = "X"
            elif game.current_room.search_grid(self.x - 1, self.y) == "E":
                game.current_room.change()
            else:
                print("Move not available!")
        elif dcs.upper() == "S":
            if game.current_room.search_grid(self.x, self.y + 1) == ".":
                game.current_room.layout[self.y][self.x] = "."
                self.y += 1
                game.current_room.layout[self.y][self.x] = "X"
            elif game.current_room.search_grid(self.x, self.y + 1) == "E":
                game.current_room.change()
            else:
                print("Move not available!")
        elif dcs.upper() == "D":
            if game.current_room.search_grid(self.x + 1, self.y) == ".":
                game.current_room.layout[self.y][self.x] = "."
                self.x += 1
                game.current_room.layout[self.y][self.x] = "X"
            elif game.current_room.search_grid(self.x + 1, self.y) == "E":
                game.current_room.change()
            else:
                print("Move not recognised!")
        elif dcs.upper() == "E":
            self.get_inv()
        else:
            print("Choice does not exist!")
    def choice_inv(self):
        item_used = None
        self.get_inv()
        dcs = input(f"1 - {self.inv[0]}, 2 - {self.inv[1]}, 3 - {self.inv[2]}, 4 - {self.inv[3]}, 5 - {self.inv[4]}  ")
        if int(dcs) in (1, 2, 3, 4, 5):
            item_used = self.inv[int(dcs) - 1]
        if item_used == "Rusty Dagger":
            print("You are already using that!")
            self.choice_inv()
        elif item_used == "Glass Shard (x2 ATTACK)":
            game.monster.hp -= self.atk * 2
            self.inv[int(dcs) - 1] = None
            print(f"You attacked the {game.monster.name} for {self.atk * 2} damage!")
        elif item_used == "Healing Potion (+10 HEALTH)":
            self.hp = min(self.max_hp, self.hp + 10)
            print(f"Healed yourself to {self.hp} HP!")
            self.inv[int(dcs) - 1] = None
        else:
            print("Item does not exist...")
            self.choice_inv()

    def choice_fight(self):
        print(f"Monster Hp = {game.monster.hp}, Your HP = {self.hp}")
        dcs = input("1 - Attack, E - Open Inventory  ")
        if dcs == "1":
            game.monster.hp -= self.atk
            print(f"You attacked the {game.monster.name} for {self.atk} damage!")
        elif dcs.upper() == "E":
            self.choice_inv()
        elif dcs != "1" and dcs.upper != "E":
            print("Move not recognised!")
        atk_chance = random.randint(1,4)
        if atk_chance == 4:
            print(f"The {game.monster.name} failed to attack you!")
        else:
            self.hp -= game.monster.atk
            print(f"The {game.monster.name} attacked you for {game.monster.atk} damage!")
        if self.hp < self.max_hp:
            self.hp += 1
    
    def lvl_up(self):
        self.atk += 1
        self.max_hp += 2
        self.hp = min(self.max_hp, self.hp + 3)
    
    def item_chance(self):
        result = random.randint(1, 50)
        if result < 10:
            self.add_item("Healing Potion (+10 HEALTH)")
            print("The phantom dropped a Healing Potion!")
        elif result < 20:
            self.add_item("Glass Shard (x2 ATTACK)")
            print("The phantom dropped a Glass Shard!")

class Monster:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk
    def get_stats(self):
        print(f"{self.name}, {self.hp}, {self.atk} <--- Monster Stats")
    
def win():
    return game.player.hp > 0


#testing
game = Game()
game.load_rooms()
game.add_player()
# player.add_item("Rusty Dagger")
# player.add_item("Glass Shard (x2 ATTACK)")
# player.add_item("Healing Potion (+10 HEALTH)")
# player.add_item("Healing Potion (+10 HEALTH)")

while game.is_not_over:
    if game.ph_encounter == 0:
        print("YOU ARE IN A FIGHT")
        print("YOU ARE IN A FIGHT")
        while game.ph_encounter == 0:
            game.player.choice_fight()
            if game.monster.hp <= 0:
                game.ph_encounter = random.randint(4, 7)
                game.add_monster(Monster("Phantom", 7 + 3 * game.room_multi, 1 + 2 * game.room_multi))
                print("Fight over.")
                print("")
                game.player.lvl_up()
                game.player.item_chance()
                print(f"You levelled up! Your attack is now {game.player.atk} and your maximum health is now {game.player.max_hp}!")
                print("")
    if game.current_room == game.attic:
        if game.player.x == 6:
            game.monster = Monster("Wraith", 50, 10)
            print("A rustle from behind you pierces the silence.")
            time.sleep(1)
            print("A ghastly being protrudes from the furniture,")
            time.sleep(1)
            print("an uncertain portrayal of a person.")
            time.sleep(1)
            while game.monster.hp > 0 and game.player.hp > 0:
                game.player.choice_fight()
            game.is_not_over = False
            win()
            break
    game.current_room.get_layout()
    game.player.choice_move()
