from os import system


def clear():
    _ = system('clear')


# 클래스 : 설계도 + 설명서 => 객체, 인스턴스, 대문자로 시작
# self : 객체 자신을 의미, this 와 동일한 의미
# 메소드를 정의할 때 처음 전달값은 반드시 self
# 메소드 내에서는 self.name 과 같은 형태로 멤버변수를 사용

class BlackBox:

    def __init__(self, name, price):  # 생성자
        self.name = name  # 맴버변수
        self.price = price  # 맴버변수


class VideoMaker:
    def make(self):
        print('추억용 여행 비디오 제작')


class MailSender:
    def send(self):
        print('메일을 발송하였습니다.')


# 클래스 상속 및 다중상속
class TravelBlackBox(BlackBox, VideoMaker, MailSender):
    def __init__(self, name, price, sd):
        super().__init__(name, price)  # 부모 클래스 __init__ 메소드 사용, super 대신, 부모 이름 (BlackBox) 사용가능
        self.sd = sd

    def set_travel_mode(self, _min):
        print(f'{self.name} - {str(_min)} 여행모드 ON - {self.price} / {self.sd} GB')


# 클래스 상속 후 매소드 재정의 : 부모의 메소드를 같은 이름으로 설정시 자동 overriding
class AdvancedTravelBackBox(TravelBlackBox):
    def set_travel_mode(self, _min):
        print(str(_min) + ' 분 동안 여행모드 ON')
        self.make()  # 추억용 여행 영상 제작
        self.send()  # 메일발송 까지 함께 작업으로 재 정의


# 객체생성방식
b1 = BlackBox('까망이', 20000)
b1.sec = 'Hided member'  # 독립적인 맴버변수 설정, 다른 객체와 차별됨
print(b1.name, b1.price, b1.sec)

b2 = TravelBlackBox('하양이', 25000, 128)
b2.set_travel_mode(55)
b2.make()
b2.send()

b3 = AdvancedTravelBackBox('빨강이', '3000', 250)
b3.set_travel_mode(125)

# b2 = BlackBox('하양이', 100000)
# print(b2.name, b2.price)

# 객체의 인스턴스 타입 확인
print(isinstance(b1, BlackBox))

clear()


# pass : 나중에 작업할 내용

# 예외 처리
# try:
#     result = num1 + num2
# except:
#     print('오류 발생')
# else:
#     pass
# finally:
#     pass
def calc(num1, num2):
    try:
        result = num1 / num2
        print(f'연산 결과는 {result} 입니다.')

    except ZeroDivisionError as ex:
        print(f'0 으로 나눌 수 없습니다.', ex)
    except TypeError as ex:
        print(f'숫자형 타입이 아닌 요소가 있습니다.')
    except Exception as ex:  #
        print(f'오류가 발생: {ex}')

    else:
        print('정상 처리 되었습니다.')

    finally:
        print('마칩니다.')


calc(12, 0)

clear()
# 모듈 : 하나의 파이썬 파일, 변수나 함수 클래스 등이 정의되어 있을 수 있음
# 패키지 : 하나의 폴더, 모듈들의 집합
# import 모듈  => 전체를 가져오는 것
# from 모듈 import 변수, 함수, 클래스  => 필요한 것만 가져올 때
# from pkgViv.hello import Friend
# friend = Friend('길산', 29)
# friend.say_hello()

from pkgViv.hello_world import HelloWorld

h = HelloWorld(1, '장길산', 33)
h.say()
