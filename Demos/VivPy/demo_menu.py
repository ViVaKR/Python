list = [ (i, f'\t{j}') for i, j in enumerate(['1. 고구마 피자', '2. 불고기피자', '3. 치즈 피자', '4. 감자 피자', '5. 종료'])]
menu_number = []

# (3) 메뉴선택의 올바름 체크 메서드
def check_menu(choice):
  # 메뉴판에 있는 것이 아닌 다른거 선택하면
  # 무한 백룸
  while choice not in menu_number:
    print('잘못된 메뉴선택입니다.')
    print_menu()
  # 한줄 뛰어쓰기 모양내기
  print()
  # 종료 선택시 퇴장하기
  if choice == 5:
    print('\t주문을 취소하고 매장을 나갑니다!!!!')
    return True
  else:
    # 선택한 메뉴 주문 확인하고 요금 받고 프로그램 마치기
    print(list[choice - 1][1] + " 메뉴를 선택하셨습니다.\n\t=> 요금은 선불입니다. (>> * <<)")
    return True
    
# (2) 메뉴선택 하기
def print_menu():
  for i in list:
    menu_number.append(i[0]+1)
    print(i[1])
    
  choice = int(input(f'\n\t메뉴를 선택하세요 => '))
  # 선택 확인 메서드 호출부...
  result = check_menu(choice)
  if result:
    exit()

# (1) 프로그램 시작점
print_menu()
