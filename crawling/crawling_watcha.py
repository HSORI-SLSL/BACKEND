from selenium import webdriver
from selenium.webdriver.common.by import By

def crawl_watcha():
    # Chrome 드라이버 실행 경로 설정
    driver_path = 'path/to/chromedriver'

    # Chrome 드라이버 초기화
    driver = webdriver.Chrome()

    # 페이지 로드
    driver.get('https://pedia.watcha.com/ko-KR/search?query=%EC%84%B8%EC%A2%85%EB%8C%80%EC%99%95&category=contents')

    # 요소 탐색
    elements = driver.find_elements(By.CLASS_NAME, 'css-usdi1z')

    # 각 요소의 텍스트 출력
    for element in elements:
        print(element.text)

    # 드라이버 종료
    driver.quit()
