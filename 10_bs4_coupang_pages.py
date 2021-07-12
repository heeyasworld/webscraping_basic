import requests
import re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}

for i in range(1, 6):
    # 1page ~ 5page(1이상 6미만)
    # print("Page No.", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(
        i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

    for item in items:
        # 광고 제품 제외
        ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
        if ad_badge:
            # print("  <광고 상품 제외합니다>")
            continue
            # continue하면 이 상품은 제외하고 진행된다

        name = item.find("div", attrs={"class": "name"}).get_text()  # 제품명

        # LG 노트북 제외하기
        if "LG" in name:
            # print("  <LG전자 상품 제외합니다>")
            continue

        price = item.find(
            "strong", attrs={"class": "price-value"}).get_text()+"원"  # 가격

        # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
        rate = item.find("em", attrs={"class": "rating"})  # 평점
        if rate:  # rate 값이 있으면(평점이 없는 상품들도 있음)
            rate = rate.get_text()
        else:
            # print("  <평점 없는 상품 제외합니다>")
            continue  # 제외하고 진행

        rate_cnt = item.find(
            "span", attrs={"class": "rating-total-count"})
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1]
        else:
            # print("  <평점 수 없는 상품 제외합니다>")
            continue  # 제외하고 진행

        link = "http://www.coupang.com" + \
            item.find("a", attrs={"class": "search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            # float(rate)해주는 이유는 rate값이 str이라서 소숫점 숫자로 데이터타입 변경
            # rate_cnt 도 str => int값으로 변경후 진행
            # print(name, price, rate+"평점", "리뷰 총"+rate_cnt+"개")
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 {rate_cnt}개")
            print(f"링크 : {link}")
            print("-"*100)  # 제품구분위해 줄긋기
