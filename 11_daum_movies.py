import requests
from bs4 import BeautifulSoup

for year in range(2016, 2021):  # 2016-2020
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(
        year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class": "thumb_img"})

    for idx, image in enumerate(images):
        image_url = image["src"]
        if image_url.startswith("//"):  # image_url이 // 으로 시작한다면 아래처럼 바꿔줘라
            image_url = "https:" + image_url

        print(image_url)

        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)
            # image_res의 content정보(이미지)를 파일로 쓴다

        if idx >= 4:  # 상위 5개 이미지까지만 다운로드 받겠다
            break
