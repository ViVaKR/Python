# Syntax of a while loop
"""
-	while some_condition_is_true:
-		do_something
-		do_something
		
-	carry_on_with_program 
"""

i = 1

# loop until we reach ... ?

while i <= 10:
    square = i * i
    print("The square of " + str(i) + " is " + str(square))

    # increment i
    i += 1
else:
    print("Exit Loop")

print("That's it")

# break

counter = 0

while True:
    counter += 1

    # test if gone too far
    if counter >= 100:
        break
    if counter % 3 != 0:
        continue

    print(counter, "Fizz")

print("break done")


i = 0
while i <= 10:
    print("The cube of {0:2} is {1:4}".format(i, i**3))
    i += 1

i = 0
while i <= 10:
    print("The Reciprocal of {0:2} is {1:.2f}".format(i, i / 3))
    i += 1
