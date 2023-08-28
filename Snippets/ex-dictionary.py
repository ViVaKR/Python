# 딕셔너리
product = {
    "제품명": "사과",
    "가격": 3000,
    "분류": "과일",
    10: 10* 3,
    True: False
}

## 키를 통한 값 출력
print(product["제품명"]) # "사과"
print(product["가격"]) # 3000
print(product["분류"]) # "과일"
print(product[10]) # "과일"
print(product[True]) # "과일"

## dic for loop
for key in product:
    print(key)
    print(product[key])
    print("-" * 20)


products = [{
    "제품명": "사과",
    "가격": 3000,
    "분류": "과일"
    }, {
    "제품명": "바나나",
    "가격": 2300,
    "분류": "과일"
    }
]

for product in products:
    for key in product:
        print(key,product[key])
    print("*" * 20)
    
