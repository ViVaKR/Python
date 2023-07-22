# Ranges Start At 0
# 1 Argument
first_ten = range(10)

for i in first_ten:
    print(i)

# 2 Argument
# ranges miss out the last term

for j in range(1, 11):
    print(j)


# 3 Argument
for k in range(3, 100, 3):
    print(k)


for m in range(10, 0, -1):
    print(m)

for i in range(1, 101):
    print("The cube of {0} is {1}".format(i, i **3))


