#! /usr/bin/env python

import os
import shutil
import glob
import sys
import re
import math

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

"""
print("Hello World")
glob (global) : 글로브 패턴
- 파일 이름의 집합을 wildcard characters 로 명시하는 패턴을 말함
* - 길이와 상관없이 모든 문자열을 매칭함.
? - 어떤 글자든 1글자만 매칭됨
[abc] - 괄호 안에 있는 글자 중에 있다면 매칭됨
[a-z] - 범위 내에 있는 글자면 매칭
[0-9] - 숫자범위 매칭
[!abc] - 괄호에 있는 문자가 없어야 매칭됨
"""
