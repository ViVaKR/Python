import random

top_of_range = input(f"Type a number\n\033[38;5;205m\u26DF  ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("\033[38;5;196mPlease type a number larger than 0 next time.\033[0m")
        quit()

random_number = random.randint(0, top_of_range)
print(f"\033[0m\t{random_number}")

guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("\033[38;5;196mPlease type a number next time.\033[0m")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")


print(f"You got it in {guesses} guesses")
