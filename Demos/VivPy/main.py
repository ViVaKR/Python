#_*_coding: utf-8 _*_

# a = int('2')
# b = int('5')
# c = float('1.5')
# print(a + b + c)
# print(5 % 2)
# print(3<5 and 7 < 5)
# print('c' in 'cat')
# print(bool(None))
# lang = 'Python'
# print(lang[:3])
# letter = 'how are YOU'
# print(letter.lower())
# print(letter.capitalize())
# print(letter.split(' '))
# str = '나도 학생 .입니다.  '
# print(str.startswith('나도'))
# print(str.endswith('학생'))
# print(str.strip('.').strip())
# print(str.replace('학생', '직장인'))
# ss = '나도직장인'
# print(ss.find('도'))
# print(ss.center(50,'-'))
# p = 'Python'
# c = "C#"
# print('개발언어에는 {1} {0} 등이 있어요'.format(p, c))
# print(f"{1+3}")

import re

# if a > b > c > d > e:
#   print("첫번째")
# elif a > b > c > d:
#   print("두번째")
# elif a > b > c:
#   print("세번째")
# elif a > b:
#   print("네번째")
# else:
#   print("다섯번째")
  
# if max(list) == a: print("첫번째")

# print(list.sort(reverse=False))

# def excute(number):
#   match number:
#     case 5: return str(number)
  
    
  
# a = 20
# b = 18
# c = 5
# d = 15
# e = 9
# list = [a, b, c, d, e]
# print(list)
# temp = sorted(list,reverse=True)
# print(temp)
# # k = 0
# # for i in range(1, len(list)):
# #   if(list[:i] == sorted(list,reverse=True)[:i]):
# #     k = i
    

# res = [i for i, e in enumerate(temp) if e != list[i]]
# print(res[0])
# match res[0]:
#   case 1: 
#     print()
#   case 2:
#     print("2")
#   case 3:
#     print("3")
#   case 4:
#     print("4")
#   case 5:
#     print("5")
    
    
# member = [['kim', 'A형', 25],['lee', 'B형', 35],['park', 'AB', 45],['choi', 'O형', 55],['jung', 'A형', 65]]
# idx = []
# for i in range(len(member)):
#   if member[i][2] < 50 :
#     idx.append(i)
# desc = sorted(idx, reverse=True)
# for i in desc:
#   del member[i]
# print(member)

# 소수판별 함수(2이상의 x 자연수 대상)
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어지면
        if x % i == 0:
            return False # !소수
    return True # 소수

# (1) 소수 판별 실행 파트
max_number = 100
print(f'{max_number} 까지 소수를 찾습니다.')
for number in range(max_number + 1):
  if is_prime_number(number):
    print(f'{number} 는 소수입니다.')
  else:
    print(f'{number} 는 소수가 아닙니다.')
