#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from Iter import Reverse
import os
import subprocess
import sys
import time
import json

print("Start")

useless_cat_call = subprocess.Popen(
    ["cat"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)
output, errors = useless_cat_call.communicate(input="Hello from the other side!")
useless_cat_call.wait()
print(output)
print(errors)


r = Reverse("egg spam")
iter(r)

for char in r:
    print(char, end="\n")

r.Etc()


def rv(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for c in rv("hello world"):
    print(c)

rs = sum(i * i for i in range(10))
print("1 to 10 * ! = ", rs)

xvec = [10, 20, 30]
yvec = [7, 5, 3]
r = sum(x * y for x, y in zip(xvec, yvec))

print("zip sum = ", r)


data = "golf"

rs = list(data[i] for i in range(len(data) - 1, -1, -1))

print("list = ", rs)
