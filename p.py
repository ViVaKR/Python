input_id = input('아이디를 입력하여 주세요\n')
input_pwd = input('비밀번호를 입력하여 주세요\n')

real_id = "Buddham"
real_pwd = "burm9037"

if real_id == input_id and real_pwd:
    print('Welcome ' + input_id)
else:
    print("로그인에 실패 하였습니다.")

