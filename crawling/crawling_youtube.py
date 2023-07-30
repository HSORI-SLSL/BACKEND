from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def crawl_youtube_contents():
    # Chrome 드라이버 실행 경로 설정
    driver_path = 'path/to/chromedriver'

    # Chrome 드라이버 초기화
    driver = webdriver.Chrome()

    # 페이지 로드
    driver.get('https://www.youtube.com/results?search_query=%EC%84%B8%EC%A2%85%EB%8C%80%EC%99%95')

    # 요소 대기
    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.style-scope.ytd-video-renderer')))

    # 각 요소의 텍스트를 리스트에 저장
    video_titles = [element.text for element in elements]

    # 드라이버 종료
    driver.quit()

    # 중복 제거 후 각 요소의 텍스트 출력
    unique_titles = list(set(video_titles))
    for title in unique_titles:
        print(title)
