class Viv:

    def __init__(self, *args):
        if len(args) == 2:
            self.name = args[0]
            self.age = args[1]
        else:
            self.name = "Vivakr"
            self.age = "25"

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Complex:

    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def display(self):
        print("Real:", self.real)
        print("Imaginary:", self.imag)


class Person:

    def __init__(self, name):
        self.name = name
        self.Peopole = []

    def Add_Person(self, name):
        self.Peopole.append(name)


class Bag:

    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


# 인스턴스 객체 : 어트리뷰트를 가지고 있는 객체, 데이터 어트리뷰트, 메서드 어트리뷰드
