from selenium import webdriver
from selenium.webdriver.common.by import By
import time

query = '세종대왕'
options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

# watcha.com의 검색 결과 페이지를 크롤링하는 코드를 작성합니다.
url = f'https://pedia.watcha.com/ko-KR/search?query={query}&category=contents'
driver.get(url)
time.sleep(2)  # 페이지 로딩을 기다립니다.

contents = []

# 각 컨텐츠의 정보를 크롤링합니다.
elements = driver.find_elements(By.CLASS_NAME, "css-8y23cj")
for element in elements:
    title = element.find_element(By.CLASS_NAME, "css-31iyzt").text
    info = element.find_element(By.CLASS_NAME, "css-1thqxgo").text
    img_url = element.find_element(By.CLASS_NAME, "css-31iyzt").get_attribute("src")
    category = element.find_element(By.CLASS_NAME, "css-qhzw1o-StyledImg ezcopuc1").text

    content = {
        "title": title,
        "info": info,
        "img_url": img_url,
        "category": category
    }
    contents.append(content)

driver.quit()
print(contents)
