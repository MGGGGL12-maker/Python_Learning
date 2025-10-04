# Python Jokenpo Game
from random import choice

options = ("ROCK", "PAPER", "SCISSORS")
running = True

while running:
    player = None
    machine = choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").upper().strip()

    print(f"Player: {player} \nComputer: {machine}")

    if player == machine:
        print("It's a tie!")
    elif player == "ROCK" and machine == "SCISSORS":
        print("You win!")
    elif player == "PAPER" and machine == "ROCK":
        print("You win!")
    elif player == "SCISSORS" and machine == "PAPER":
        print("You win!")
    else:
        print("You lose!")
 
    if input("Play again (Y/N): ").upper() == "N":
        running = False

print("Thanks for playing!")