import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input(
        "Type Rock/Paper/Scissors or Q to quit.\n\033[031m\u26DF  "
    ).lower()
    print("\033[0m\n")

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2

    computer_pick = options[random_number]
    print("Computer picked", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("Is Same")
        continue
    else:
        print("You lost!")
        computer_wins += 1

print(
    f"\033[031mYou won\t\t({user_wins}) times\nComputer won\t({computer_wins}) times\033[0m"
)
print("Goodbye!")
