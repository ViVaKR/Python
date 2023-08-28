def say():
    print('안녕 방가방가웡!!!')


class Friend:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'안녕! 나의 친구 {self.name} 반가워')
        print(f'너의 나이도 벌써 {self.age} 이되었구나..')