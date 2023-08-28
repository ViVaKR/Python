numbers = [273, 103, 5, 38, 64, 9, 82, 800, 99]

for number in numbers:
    # 홀수 짝수
    if number % 2 == 0:
        print(f"{number} 은/는 짝수입니다.")
    else:
        print(f"{number} 은/는 홀수입니다.")
    # 자릿수 출력
    print(f"{number} 은/는 {len(str(number))} 자리입니다.")
    print()

## 1차원 리스트를 주지적으로 반복되는 값으로 2차원 배열 작성 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output =  [[], [], []]
""" 목표 결과
output[0] = [1, 4, 7]
output[1] = [2, 5, 8]
output[2] = [3, 6, 9] 
"""

for number in numbers:
    # 주기적으로 반복되는 것은 `%` 나머지 연산자 사용
    # (예) number = 1 -> 1 % 3 = 1, 목표값: 0
    output[(number - 1) % 3].append(number)

print(output)
