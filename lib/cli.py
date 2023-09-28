# lib/cli.py

from models.models import Player, Score
from trivia_db import trivia_db
###

from helpers import (
    exit_program,
    initialize,
    create_player,
    get_all_players,
    update_player_username_by_id,
    delete_player_by_id
)

import random




#####
# def guess_fav_num_game():

#     print("Enter your Username.")
#     username = input('>>> ')
#     players = [player for player in Player.all if player.username == username]
#     if len(players) > 0:
#         player = players[0]
#         print(f'Welcome Back {player.username}')
#     else:
#         player = Player.create(username)
#         print(f'Hello new player!')

#     # HIGHEST_VALUE = int(input("Enter the highest range for random number: "))
#     HIGHEST_VALUE = 100
#     random_number = random.randint(1, HIGHEST_VALUE)

#     guesses = 0
#     user_guess = 0

#     while True:
#         user_guess = input("Guess my favorite number: ")
#         guesses += 1

#         if not user_guess.isdigit():
#             print("Error: Value is not a number. Please enter a numeric value")
#         elif int(user_guess) not in range(1, HIGHEST_VALUE + 1):
#             print("Error: Value is outside of guessing range!")
#         else:
#             if random_number == int(user_guess):
#                 print("Correct! Wow you sure are a mind reader!")
#                 break
#             elif int(user_guess) > random_number:
#                 print("Nope, too high!")
#             else:
#                 print("Nope, too low!")

#     score = round(float(1000 / guesses), 1)
#     print(f"You guessed it in {guesses} guesses. Your score is: {score}")

#     Score.create(player.id, score)
#####







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

        # print(user_guess)
        
        while user_guess.lower() != (current_trivia_dict['correct_answer'].lower()):
            strikes -= 1
            # print(current_trivia_dict['correct_answer'])
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
        # # elif choice in ["r1", "R1"]:
        # #     get_hotel_by_id()
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
    print("R - Get all player_scores")
    print("U - Update player by ID")
    print("D - Delete player by ID")
    print("Q - Exit the program")


if __name__ == "__main__":
    initialize()
    main()

