import requests

# 캐시용 딕셔너리 초기화
cache = {}

def crawl_watcha_contents(query, use_cache=True):

    if use_cache and query in cache:
        return cache[query]

    # API 엔드포인트 URL
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}'

    # JSON 데이터를 담을 리스트
    contents_list = []

    try:
        # API에 GET 요청 보내기
        response = requests.get(url)
        response.raise_for_status()  # 요청이 성공적인지 확인

        # JSON 응답 파싱
        data = response.json()

        # 도서 정보 추출
        books = data.get('items', [])

        # 각 도서 정보 출력
        for book in books:
            title = book['volumeInfo']['title']
            authors = ', '.join(book['volumeInfo']['authors'])
            thumbnail_info = book['volumeInfo'].get('imageLinks', {})
            thumbnail = thumbnail_info.get('thumbnail', 'No Image')
            content = {
                "title": title,
                "authors": authors,
                "thumbnail_info": thumbnail_info,
                "thumbnail": thumbnail  # 이미지 URL 추가
                #"href": href  # 링크 추가
            }
            contents_list.append(content)

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

    # 캐시에 데이터 저장
    cache[query] = contents_list

    return contents_list

'''def crawl_watcha_contents(query, use_cache=True):
    if use_cache and query in cache:
        return cache[query]

    query = query

    # Chrome 드라이버 초기화
    # ChromeOptions를 사용하여 ChromeDriver 경로 설정
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chromedriver.exe"
    chrome_options.add_argument("--no-sandbox")

    # Chrome 드라이버 초기화
    driver = webdriver.Chrome(executable_path="C:/path/to/chromedriver.exe", chrome_options=chrome_options)

    # 페이지 로드
    url = 'https://pedia.watcha.com/ko-KR/search?query=' + query + '&category=contents'
    driver.get(url)

    # 요소 탐색
    #elements = driver.find_elements(By.CLASS_NAME, 'css-1s4ow07')
    elements = driver.find_elements(By.CLASS_NAME, 'css-1ofozqs')

    # JSON 데이터를 담을 리스트
    contents_list = []

    for element in elements:
        # 텍스트 가져오기
        text = element.text

        # 이미지 URL 가져오기
        img_tags = element.find_elements(By.TAG_NAME, 'img')
        img_urls = [img.get_attribute('src') for img in img_tags]

        # 링크 가져오기
        a_tags = element.find_elements(By.TAG_NAME, 'a')
        hrefs = [a.get_attribute('href') for a in a_tags]

        # 텍스트를 줄바꿈 문자 기준으로 분리하여 정보 추출
        lines = text.split('\n')
        for i in range(0, len(lines), 3):
            title = lines[i]
            info = lines[i + 1]
            category = lines[i + 2]
            img_url = img_urls[i // 3]
            href = hrefs[i // 3]

            # 각 정보를 딕셔너리로 만들어 리스트에 추가
            content = {
                "title": title,
                "info": info,
                "category": category,
                "img_urls": img_url,  # 이미지 URL 추가
                "href": href  # 링크 추가
            }
            contents_list.append(content)

    # 드라이버 종료
    driver.quit()

    # 캐시에 데이터 저장
    cache[query] = contents_list

    return contents_list'''