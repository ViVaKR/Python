from VivClass import Viv, Complex, Person


def main():

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

    print(people.Peopole)


main()
