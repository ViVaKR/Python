keyboard = ['도', '레', '미', '파', '솔', '라', '시']
key1 = [0, 2, 4]
key4 = [3, 5, 0]
key5 = [4, 6, 1]

key = []
def getKeys(ch):
    global key
    match ch:
        case 1:
            key = key1
        case 4:
            key = key4
        case 5:
            key = key5

choice = 0
category = [1, 4, 5]
while choice not in category:
    choice = int(input('화음을 선택하세요(1/4/5) : '))
    if choice not in [1, 4, 5]:
        print('잘못된 선택입니다! 다씨.. ')

getKeys(choice)

def intersection(lst1, lst2):

    lst3 = [(i, j) for (i,j) in enumerate(lst1) if i in lst2]
    lst = []
    for i in lst2:
        for ij, n in lst3:
            if i == ij:
                lst.insert(lst2.index(i), n)

    return lst

print(intersection(keyboard,key))