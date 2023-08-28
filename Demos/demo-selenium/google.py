from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request  # 다운로드

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element(By.NAME, "q")
elem.send_keys("파이썬")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 3
# javascript 명령어를 실행하여 현재 스크롤 높이를 last_height 에 저장
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # scroll down to bottom, 브라우저 끝까지 스크롤을 내리는 명령어
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # wait to load page, 로드 되는 시간 까지 대기
    time.sleep(SCROLL_PAUSE_TIME)

    # 다시 브라우저의 높이를 구함
    new_height = driver.execute_script("return document.body.scrollHeight")

    # 내렸는데 더이상 내려가지 않고 같다면? 이미지 더보기 버튼 클릭, 더 이상없다면 루프 빠져나가고
    if new_height == last_height:
        try:
            button = driver.find_element(By.CSS_SELECTOR, ".mye4qd")
            button.click()
        except:
            # 더이상 더보기 버튼이 없어 오류 발생시 루프 벗어나기
            break

    # 같지 않다면 저장하고 계속 반복 스크롤링
    last_height = new_height

images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(SCROLL_PAUSE_TIME)
        # rs = driver.find_element(By.CSS_SELECTOR, ".n3VNCb").get_attribute("src")
        imgUrl = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, f"download/images/demo_{count}.jpg")
        count += 1
    except:
        pass

print(f"{count} 개 사진 다운로드 완료")
driver.close()
