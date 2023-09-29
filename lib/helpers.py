# lib/helpers.py

from models.models import Player, Score

def helper_1():
    print("Performing useful function#1.")

def initialize():
    Player.create_table()
    Player.get_all()
    Score.create_table()
    Score.get_all()

def create_player():
    print("Enter username for new player:")
    player_username = input(">>> ")
    while not player_username:
        print("Error: Name cannot be blank!")
        print("Enter username for new player:")
        player_username = input(">>> ")
    new_player_username = Player.create(player_username)
    print("Player username added!")
    print(new_player_username)
    keyboard_input = input("* Press 'enter' to continue *\n")

def get_all_players():
    if len(Player.all) == 0:
        print("Error: No players in the database!")
    else:
        for player in Player.all:
            print(player)
        print("Obtained player data.")
        keyboard_input = input("* Press 'enter' to continue *\n")

def get_all_scores():
    if len(Score.all) == 0:
        print("Error: No scores recorded in database!")
    else:
        for score in Score.all:
            print(score)
        print("Obtained score data.")
        keyboard_input = input("* Press 'enter' to continue *\n")

def update_player_username_by_id():
    if len(Player.all) == 0:
        print("Error: No players in the database!")
    else:
        player = search_by_id('update')
        print("Enter new username:")
        player_username = input(">>> ")
        while not player_username:
            print("Error: Username cannot be blank!")
            print("Enter new username:")
            player_username = input(">>> ")
        player.username = player_username
        player.update()
        print(player)
        print("Username updated!")
        keyboard_input = input("* Press 'enter' to continue *\n")

def delete_player_by_id():
    if len(Player.all) == 0:
        print("Error: No players in the database!")
    else:
        player = search_by_id('delete')
        player.delete()
        print(f"Player deleted!")
        keyboard_input = input("* Press 'enter' to continue *\n")

def search_by_id(word):
    print(f"Enter the player id that you want to {word}:")
    id = input(">>> ")
    
    if id.isdigit():
        player = Player.find_by_id(int(id))
    else:
        player = None
    
    while not player:
        print("Error: Player id not found!")
        print(f"Enter the player id that you want to {word}:")
        id = input(">>> ")

        if id.isdigit():
            player = Player.find_by_id(int(id))
        else:
            player = None

    return player

def exit_program():
    print("Exiting program. See you next time!")
    exit()






















