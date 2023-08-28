import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


address_book = {}


def main():
    while True:
        sel = display_menu()

        if sel == 1:
            insert()
        elif sel == 2:
            delete()
        elif sel == 3:
            search()
        elif sel == 4:
            print(f'연락처 총 ({len(address_book)}) 명')
            for key in address_book.keys():
                print_address(key)
        else:
            break


def display_menu():
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")
    sel = int(input("메뉴 항목을 선택하시오 : "))
    return sel


def insert():
    name = input('이름 : ')
    phone = input('전화번호 : ')
    address_book[name] = phone
    print_address(name)


def print_error():
    print("Error : 주소록에 없는 이름!")


def delete():
    name = input("삭제할 이름 입력: ")
    if name in address_book:
        del address_book[name]
    else:
        print_error()


def search():
    name = input('검색할 이름 입력: ')
    phone = address_book.get(name, 'Error : 주소록에 없는 이름!.')
    print(f'{name}:', phone)


def print_address(key):
    if not address_book: return
    message = f'{key}의 전화번호: {address_book[key]}'
    print(message)
    print(''.join(['=' for i in range(len(message) + 2)]))


try:
    main()
except:
    pass
