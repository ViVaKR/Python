s= 0

for x in range(2, 20): # (1) 2 ~ 19 (18번 반복)
    for y in range(1, 10): # (2) 1 ~ 9 (9번 반복)
        s = s + 1

print(s) # result => 162

# 즉, x 에서 (2 ~ 19) 각 회당 , 내부 y 에서 9번 반복하므로 => 18 * 9 => 최종 :  162
