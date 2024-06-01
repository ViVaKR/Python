#! /usr/bin/env python

import os
import shutil
import glob
import sys
import re
import math
import statistics
from datetime import date
import zlib
from timeit import Timer
import locale
from string import Template
from decimal import *


locale.setlocale(locale.LC_ALL, "")
current = os.getcwd()
print(current)
os.system("ls -l")
shutil.copy("Stdlibs.py", "Stdlibs.py.bak")

rs = glob.glob("*.py")

print(rs)

print(sys.argv)

if len(sys.argv) > 1:
    for i in range(len(sys.argv)):
        print(sys.argv[i])

sys.stderr.write("This is stderr text\n")


rs = re.findall(r"\bf[a-z]*", "which foot or hand fell fastest")
print(rs)

rs = math.sin(1)

print(
    "\n",
    rs,
    "\n",
    math.cos(1),
    "\n",
    math.tan(1),
    "\n",
    math.sin(math.pi / 2),
    "\n",
    math.sin(math.pi),
)

# 평균, 중앙값, 분산 (SciPy, NumPy 라이브러리가 더 좋음)
data = [1, 2, 3, 4, 5]
print("mean: ", statistics.mean(data))
print("median: ", statistics.median(data))
print("variance: ", statistics.variance(data))

now = date.today()
print(now)

print(date(2024, 5, 31))

birthday = date(1992, 2, 6)
age = now - birthday
print("age: ", age.days // 365)

str = b"witch which has which witches wrist watch"
l = len(str)
print("str length: ", l)
z = zlib.compress(str)
l = len(z)
print("compressed length: ", l)

z = zlib.decompress(z)
print("decompress length: ", len(z))

t = Timer("for i in range(1, 100): 1 + 1").timeit()
print(t)


conv = locale.localeconv()
print(conv)

x = 12345678
rs = locale.format_string("%d", x, grouping=True)
print(rs)
rs = locale.format_string(
    "%s%.*f", (conv["currency_symbol"], conv["frac_digits"], x), grouping=True
)
print(rs)

t = Template("Hello, $who!")
rs = t.substitute(who="Python")
print(rs)

price = round(Decimal("0.70") * Decimal("1.05"), 2)
print(price)

print(format(math.pi, ".12g"))
print(repr(math.pi))
print(math.isclose(0.1 + 0.1 + 0.1, 0.3))

print(round(math.pi, ndigits=2) == round(22 / 7, ndigits=2))

x = 3.14
print(x.hex())
x = float.fromhex("0x1.91eb851eb851fp+1")
print(x)
x = 13.0
print(x.hex())

letters = ["a", "b", "c", "d"]
print(len(letters))

a = ["a", "b", "c"]
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])

# Fibonacci

a, b = 0, 1

print(a, b, end="\n")


while a < 1000:
    print(a, end=" ")
    a, b = b, a + b
print()
