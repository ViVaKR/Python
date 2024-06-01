#! /usr/bin/env python

import sys
from VivClass import Viv, Complex, Person
import If
import Shape

arg_1 = sys.argv[1]
print(arg_1)


def main(c: int):
    print("main function", c)

    match c:
        case 1:
            print("Case 1")
            If.if_statement()
            return "If statement"
        case 2:
            myViv = Viv("IamViVaKR", "60")
            myViv.display()

            viv = Viv()
            viv.display()

            complex = Complex(123, 3.141592)
            complex.display()

            people = Person("A1")
            people.Add_Person("A2")
            people.Add_Person("A3")
            people.Add_Person("A4")
            return "Class statement"
        case 3:

            print("도형의 종류\n- (1)삼각형\n- (2)사각형\n- (3)원\n- (4)기타 도형\n")
            type = int(input())

            if type == 1:
                print("한변의 길이를 입력하세요 : ")
                length = int(input())
                Shape.DrawTriAngle(3, length)
            elif type == 2:
                print("너비를 입력하세요 : ")
                width = int(input())
                print("높이를 입력하세요 : ")
                height = int(input())
                Shape.DrawRectangle(width, height)
            elif type == 3:
                print("원의 반지름을 입력하세요 : ")
                radius = int(input())
                Shape.DrawCircle(radius)
            elif type == 4:
                print("기타 도형")
                Shape.DrawEtc()
            elif type == 5:
                print("기타 도형2")
                Shape.DrawEtc2()
            elif type == 6:
                print("기타 도형3")
                Shape.DrawEtc3()
            elif type == 7:
                print("기타 도형4")
                Shape.DrawEtc2()

            return "Shape statement"
        case _:
            return "Somthing's wrong!"


if __name__ == "__main__":
    print("This is Main.py")
    main(int(arg_1))


# --> `if __name__ == "__main__":``
#     파이썬 파일을 커맨드라인에서 직접 실행할 때는  __name__은 "__main__"이다.

# 1. Local namespace - 함수별로 구분되는 네임스페이스
# 2. Global namespace - 모듈별로 구분되는 네임스페이스
# 3. Built-in namespace - 기본 내장 함수들의 네임스페이스

# 탐색 순서 : Local -> Global -> Built-in
