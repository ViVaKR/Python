# package import
import converter  # 전체 가져오기
from converter import kg_to_lbs, find_max  # 일부만 가져오기

print(converter.lbs_to_kg(100))

print(kg_to_lbs(70))

numbers = [23, 56, 23, 82, 1, 45, 33]

print(find_max(numbers))


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoning")


dog = Dog()
dog.walk()
dog.bark()

cat = Cat()
cat.walk()
cat.be_annoying()


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John")
print(john.name)
john.talk()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print(f"{self.x} move")

    def draw(self):
        print(f"{self.y} draw")


# point = Point(10, 20)
# point.x = 11
# print(point.x)

# exception (exit code no error = 0)
# try:
#     age = int(input('Age: '))
#     income = 20_000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print(f"Age cannot be 0.")
# except ValueError:
#     print(f'Invalid value')


# def emoji_eonverter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "😆",
#         ":(": "☹️"
#     }
#
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# msg = input("> ")
# print(emoji_eonverter(msg))

# 기본적으로 None 을 리턴함
# def squar(number):
#     print(number * number)
#

# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}')
#     print('Welcome aboard')
#
#
# print("Start")
# # position argument, keyword argument
# greet_user(last_name="Smith", first_name="John")
# print("Finish")


# dictionary
# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
#
# print(customer.get("name"))
# print(customer["name"])
# customer["name"] = "Jack Smith"
# print(customer["name"])
# print(customer.get("birthday", "Jan 1 1980"))   # 값이 없으면 기본값을 가져옴
# customer["birthday"] = "Jan 1 1980"

# phone = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Five"
# }
#
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
#
# print(output)

# message = input("> ")
# words = message.split(" ")
# emojis = {
#     ":)": "😆",
#     ":(": "☹️"
# }
#
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
#
# print(output)

# Tupple : 불변형
# numbers = (1, 2, 3)
# print(numbers[0])
#
# coordinates = (1, 2, 3)
# x, y, z = coordinates
# print(x)
# print(y)
# print(z)

# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
#
# print(uniques)

# nums = [5, 2, 1, 5, 7, 4]
# nums.insert(0, 10)
# nums.remove(5)
# nums.clear()
# nums.pop()
# print(50 in nums)       # boolean result => True, False
# print(nums.index(5))   # error
# print(nums.count(5))
# nums.sort()
# print(nums)
# nums.reverse()
# print(nums)
#
# nums2 = nums.copy()
# nums.append(10)
# print(nums)
# print(nums2)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix[0][1] = 20
# print(matrix[0][1])
#
# for row in matrix:
#     for item in row:
#         print(item)

# 최대값 찾기
# numbers = [3, 6, 2, 46, 1, 8, 4, 10, 58, 5, 0, 12]
# maxNumber = numbers[0]
#
# for number in numbers:
#     if number > maxNumber:
#         maxNumber = number
#
# print(maxNumber)

# for item in ['Mosh', 'John', 'Sarah']:
#     print(item)
#
# for item in range(5, 10, 2):
#     print(item)
#
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total = total + price
#
# print(f"Total: {total}")
#
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')
#
# numbers = [5, 2, 5, 2, 2]
#
# for x_count in numbers:
#     print(f"{'x' * x_count}")

# while loop
# i = 1
# while i <= 5:
#     print(' * ' * i)
#     i = i + 1
#
# print("Done")

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won!')
#         break
# else:
#     print('Sorry, you failed')

# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped")
#         else:
#             stopped = True
#             print("Car stopped...")
#     elif command == "help":
#         print("""start - to start to car
# stop - to stop the car
# quit - to quit""")
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand that!")

# if_condition
# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Waar warm clothes")
# else:
#     print("It's a lovely day")
#
# print("Enjou your day")

# price = 1_000_000
# has_good_credit = False
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
#
# print(f"Down payment: ${down_payment}")

# AND: both
# OR: at least one
# NOT
# has_high_income = True
# has_good_credit = False
# has_criminal_record = False
#
# if has_high_income or has_good_credit and not has_criminal_record:
#     print("Eligible for loan")
#
# temperature = 30
# if temperature > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")
#
# name = "Hello world"
#
# if len(name) < 3:
#     print("Name must be at least 3 characters")
# elif len(name) > 50:
#     print("Name must be a maximum of 50 characters")
# else:
#     print("looks good!")
# weight = int(input("Weight: "))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are{converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"{converted} pounds")

# import math
#
# math.ceil(2.9)
# print(math.ceil(2.9))
#
# print(math.floor(2.9))

# math function
# x = 2.9
# print(round(x))
# print(abs(-2.9))


# 연산우선순위
# parenthesis (괄호)
# exponentiation
# divisionultiplication
# addtion
# subraction
# x = 10 + 3 * 2 ** 2
# print(x)


# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)
#
# x = 10
# x += 3
# print(x)

# course = 'Python for Beginners'
# print(course.find('B'))
# print(course.find('Beginners'))
# print(course.replace('Beginners', 'Absolute Beginners'))
#
# tf = 'Python' in course     # return bool
# print(tf)
#
# print(f'title => {course.title()}')

# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course)

# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# # John [] is a coder
# print(message)
# print(msg)

# name = 'Jennifer'
# course = 'Python form Beginners'
# another = course[:]
# print(course[-1])   # 끝에서 부터
# print(course[0:3])  # 앞에서 3개
# print(course[1:])   # 1부터 끝까지
# print(course[:5])   # 0 부터 5개
# print(course[:])
# print(name[1:-1])

# - multi line
# course = '''
# Hi John
#
# Here is our firts email to you.
#
# Thank you,
#
# The support team
# '''
# print(course)

# - 형변환
weight_lbs = input("Weight (lbs): ")
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

birth_year = input("Birth year: ")
print(type(birth_year))

age = 2019 - int(birth_year)
print(type(age))
print(age)
