from selenium import webdriver
from selenium.webdriver.common.by import By
import json

def crawl_watcha_contents(query):
    driver_path = 'path/to/chromedriver'
    query = query

    # Chrome 드라이버 초기화
    driver = webdriver.Chrome()

    # 페이지 로드
    driver.get('https://pedia.watcha.com/ko-KR/search?query={query}&category=contents')

    # 요소 탐색
    elements = driver.find_elements(By.CLASS_NAME, 'css-1s4ow07')

    # JSON 데이터를 담을 리스트
    contents_list = []

    for element in elements:
        # 텍스트 가져오기
        text = element.text

        # 이미지 URL 가져오기
        img_tags = element.find_elements(By.TAG_NAME, 'img')
        img_urls = [img.get_attribute('src') for img in img_tags]

        # 텍스트를 줄바꿈 문자 기준으로 분리하여 정보 추출
        lines = text.split('\n')
        for i in range(0, len(lines), 3):
            title = lines[i]
            info = lines[i + 1]
            category = lines[i + 2]
            img_url = img_urls[i // 3]

            # 각 정보를 딕셔너리로 만들어 리스트에 추가
            content = {
                "title": title,
                "info": info,
                "category": category,
                "img_urls": img_url  # 이미지 URL 추가
            }
            contents_list.append(content)

    # 드라이버 종료
    driver.quit()

    # 최종 결과를 JSON 형식으로 출력
    print(json.dumps(contents_list, ensure_ascii=False, indent=2))

    return contents_list
