# A Quick Game of Trivia


## App Features
<li>This is a simple CLI application that allow players to play a quick game of Trivia.</li>
<li>Each player will have 3 chances to answer as many trivia questions as possible.</li>
<li>Every question that is answered correctly will add 100 points to the user's score.</li>
<li>Conversely, every question that is answered incorrectly will deduct 1 chance.</li>
<li>When the player reaches 0 chance left, the player has lost and the game ends.</li>
<li>Whichever player can answer the most trivia question correctly and obtain the highest score wins.</li>
<li>Returning players are welcome play the game again. Simply type in the same username previously entered.</li>
<li>The game continues until either the player reaches 0 chances left, or until the player decides to quit the game by pressing 'Q'.</li>


## Environment Setup Instructions
Before starting the game, you first need to install the dependencies for the program by running the following commands in the terminal:

```console
pipenv install
pipenv shell
```

Once inside pipenv shell, navigate into the file directory and cd into 'lib'.
From there, enter the following command to start the program:

```console
python cli.py
```

## Navigating through the CLI menu.
In the CLI menu shown below, select the desired operation by typing in the corresponding letter and pressing 'enter':


```console
Main Menu: Please select an option:
P - Play the game
C - Create a new player
R - View all players
S - View all scores
U - Update player by ID
D - Delete player by ID
Q - Exit the program
```


P => enter the game module to play the game

C => create a new username for new player

R => View all the existing player usernames

S => View all the scores of existing players

U => Update the player username based on player id

D => Delete a player username based on player id

Q => End the program and return to the terminal


## Resources
- https://opentdb.com/api.php?amount=10&category=17&difficulty=easy
