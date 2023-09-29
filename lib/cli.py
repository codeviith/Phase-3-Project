# lib/cli.py
from models.models import Player, Score
from trivia_db import trivia_db
from helpers import (
    exit_program,
    initialize,
    create_player,
    get_all_players,
    get_all_scores,
    update_player_username_by_id,
    delete_player_by_id
)

import random


def trivia_game():
    print("Enter your Username.")
    username = input('>>> ')
    players = [player for player in Player.all if player.username == username]
    if len(players) > 0:
        player = players[0]
        print(f'Welcome back {player.username}')
    else:
        player = Player.create(username)
        print(f'Hello new player!')

    score_instance = Score.create(player.id, 0)

    strikes = 3

    while True:
        randomNum = random.randint(1, 10)


        current_trivia_dict = trivia_db[randomNum - 1]
    
        print(current_trivia_dict['question'])
        print("Type your answer here: ")
        user_guess = input('>>> ')
        
        while user_guess.lower() != (current_trivia_dict['correct_answer'].lower()):
            strikes -= 1
            print(f"Incorrect, please try again. You have {strikes} chances left.")

            if (strikes == 0):
                print(f"Game Over, you have {strikes} chances left...Better luck next time!")
                exit()

            print("Type your answer here: ")
            user_guess = input('>>> ')
        if (current_trivia_dict['correct_answer']).lower() == user_guess.lower():
            score_instance.value += 100
            score_instance.update()
            
            print("Correct! 100 points has been added to your score!")
        

def main():
    while True:
        menu()
        choice = input(">>> ")
        if choice in ["p", "P"]:
            trivia_game()
        if choice in ["q", "Q"]:
            exit_program()
        elif choice in ["c", "C"]:
            create_player()
        elif choice in ["r", "R"]:
            get_all_players()
        elif choice in ["s", "S"]:
            get_all_scores()
        elif choice in ["u", "U"]:
            update_player_username_by_id()
        elif choice in ["d", "D"]:
            delete_player_by_id()
        else:
            print("Invalid choice")
            keyboard_input = input("* Press 'enter' to continue *\n")


def menu():
    print("Main Menu: Please select an option:")
    print("P - Play the game")
    print("C - Create a new player")
    print("R - View all players")
    print("S - View all scores")
    print("U - Update player by ID")
    print("D - Delete player by ID")
    print("Q - Exit the program")


if __name__ == "__main__":
    initialize()
    main()

