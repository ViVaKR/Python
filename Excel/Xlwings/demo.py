A = {"가": 10, "나": 20, "다": 30}
S = input("검색할 문자를 입력하세요: ")
result = A.get(S, "없음")
print(result)
