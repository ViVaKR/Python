#! /usr/bin/env python
import random

rnd = random.sample(range(1, 100), 10)
print(rnd)

rnd = random.choice(range(1, 100))
print(rnd)

rnd = random.random()
print(rnd)

rnd = random.randrange(5, 11)
print(rnd)
