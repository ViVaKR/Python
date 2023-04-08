mylist = ["apple", "banana", "cherry"]

mylist.insert(3,"Persimmon")
mylist.append("Mandarin")
mylist.insert(3,"Jujube")
mylist.insert(3,"Strawberry")
mylist.insert(3,"Lime")
mylist.insert(3,"Mango")
mylist.append("Apple")
mylist.remove("Mandarin")

for i in mylist:
    print(i)
    
if "banana" in mylist:
    print("yes")
else:
    print("no")

mylist.reverse() # 리스트 역방향
print(len(mylist)) # 리스트 길이
item = mylist.pop() # 팝 
mylist = [4, 3, 1, -1, -5, 10]
mylist.sort() # 리스트 정렬 (1)
print(mylist)
new_list = sorted(mylist) # 리스트 정렬 (2)
print(new_list)
mylist = [0] * 5 # 리스트 반복
print(mylist)
mylist2 = [1, 2, 3, 4, 5]
new_list = mylist + mylist2
print(new_list)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]
print(a)

### 보조자료 ###
""" 
Persimmon	감
Mandarin	귤
Jujube	대추
Strawberry	딸기
Lime	라임
Mango	망고
Fig	무화과
Banana	바나나
Pear	배
Peach	복숭아
Blueberry	불루베리
Apple	사과
Pomegranate	석류
Watermelon	수박
Orange	오렌지
Yuja	유자
Plum	자두
Orental Melon	참외
Kiwi	키위
Grapes	포도 
"""

""" alt + shift + a
alt + shift + a
alt + shift + a """
