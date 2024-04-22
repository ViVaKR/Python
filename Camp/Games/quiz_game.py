print("Welcom to my conputer quiz!")


def ask(message):
    return f"\033[031m{message}\033[0m\n\u27a5 "


playing = input("\033[31mDo you want to play?\033[0m\n\u27a5 ").lower()

if playing != "yes":
    quit()

print()
print("Okay! Let's play \u26bd ")
print()

score = 0

# 1
answer = input(ask("What does CPU stand for?")).lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# 2
answer = input(ask("What dows GPU stand for?")).lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# 3
answer = input(ask("What does RAM stand for?")).lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# 4
answer = input(ask("What does PSU stand for?")).lower()
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print(f"Your Score is {score} ({ (score/4) * 100}%.)")
