
import urllib.request

for i in range(11):
    try:
      # 이미지 uri
      imgUrl = f"http://www.pnst.kr/img/demo_{i}.jpg"
      # project 내 download folder 내부로 다운로드 하기
      urllib.request.urlretrieve(imgUrl, f"download/image_{i}.jpg")
    except:
        pass
      
print('다운로드 완료')

def first(a, b):
  global c
  if a > b:
    c = True
  elif a == b:
    c = None
  else:
    c = False

def second():
  if c == True:
    print("C => True, ")
  elif c== None:
    print("C => False")
  else:
        print("C => None")
    
    
def third():
  if c == True:
    print("C => True, ")
  elif c== None:
    print("C => False")
  else:
    print("C => None")

# True Test (1)
first(10 , 9)
second()

# False Test (2)
first(5, 8)
second()

# None Test (3)
first(2, 2)
third()
