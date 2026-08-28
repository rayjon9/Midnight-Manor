import game

mud = game.Game()

def test_move_room():
    """Test that when player moves east and west, they return to the same room."""
    starting_room = mud.current_room
    mud.move("D")
    intermediate_room = mud.current_room
    assert intermediate_room != starting_room, "Player did not move rooms when moving east."
    mud.move("A")
    final_room = mud.current_room
    assert final_room == starting_room, "Player did not return to starting room when moving west."

def test_invalid_move():
    """Test that when player tries to move in an invalid direction, they stay in the same room."""
    try:
        mud.move("Move not available!")
    except ValueError:
        # correct behavior
        pass
    else:
        raise AssertionError("No error raised when player moved in an invalid direction.")

def test_take_item():
    """Test that when player takes an item, it is added to their inventory."""
    starting_inventory = mud.player.inventory.copy()
    mud.take_item("Health Potion")
    assert "Health Potion" in mud.player.inventory, "Item not added to inventory when taken."
    assert len(mud.player.inventory) == len(starting_inventory) + 1, "Inventory size did not increase after taking item."

def test_hp():
    """Test that when player drinks health potion, their health increases by the correct amount."""
    starting_hp = mud.player.hp
    mud.drink_health_potion()
    assert mud.player.hp == starting_hp + 20, "Player's health did not increase by 20 after drinking health potion."

def test_attack():
    """Test that when player attacks an enemy, the enemy's health decreases by the correct amount."""
    starting_enemy_hp = mud.current_room.enemy.hp
    mud.attack_enemy()
    assert mud.current_room.enemy.hp == starting_enemy_hp - 10, "Enemy's health did not decrease by 10 after player attack."

def test_enemy_attack():
    """Test that when enemy attacks player, the player's health decreases by the correct amount."""
    starting_player_hp = mud.player.hp
    mud.enemy_attack()
    assert mud.player.hp == starting_player_hp - 5, "Player's health did not decrease by 5 after enemy attack."

def test_inventory_limit():
    """Test that when player tries to take an item when inventory is full, they cannot take it."""
    mud.player.inventory = ["Item1", "Item2", "Item3", "Item4", "Item5"]
    try:
        mud.take_item("Extra Item")
    except ValueError:
        # correct behavior
        pass
    else:
        raise AssertionError("No error raised when player tried to take item with full inventory.")

def test_use_item():
    """Test that when player uses an item, it is removed from their inventory."""
    mud.player.inventory.append("Health Potion")
    starting_inventory = mud.player.inventory.copy()
    mud.use_item("Health Potion")
    assert "Health Potion" not in mud.player.inventory, "Item not removed from inventory after use."
    assert len(mud.player.inventory) == len(starting_inventory) - 1, "Inventory size did not decrease after using item."

def test_game_over():
    """Test that game ends when player's health reaches zero."""
    mud.player.hp = 5
    mud.enemy_attack()
    assert mud.is_game_over(), "Game did not end when player's health reached zero."