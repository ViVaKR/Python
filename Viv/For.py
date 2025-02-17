#! /usr/bin/env python

words = ["cat", "window", "defenestrate"]
for w in words:
    print(w, len(w))


users = {"Hans": "active", "Jenny": "inactive", "Peter": "active"}

active_users = {}
for user, status in users.copy().items():
    if status == "inactive":
        # del users[user]
        active_users[user] = status
        continue
    print(user, status)

print(active_users)


for i in range(10):
    print(i)

l1 = list(range(5, 10))
print(l1)
l2 = list(range(0, 13, 3))
print(l2)
l3 = list(range(-10, -101, -30))
print(l3)

a = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(a)):
    print(i, a[i])


print(sum(range(11)))

# prime number
for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n // x)
            break
    else:
        print(n, "is a prime number")

# pass
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)

# pass statement
while True:
    pass


# 최소한의 클래스
class MyEmptyClass:
    pass


# 함수
def initlog(*args):
    pass
