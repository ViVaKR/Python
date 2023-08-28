
s = 0
for i in range(3333, 10000):
    if i % 1234 != 0:
        continue

    print(i)

    s += i

print(s)

