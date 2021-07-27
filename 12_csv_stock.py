import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

# csv 파일로 만들기
filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
# newline="" 공백으로 해야 우리가 원하는대로 데이터별로 한줄 줄바꿈된 채로 출력된다
# 만약 설정하지 않으면 사이에 공백이 한 줄씩 생긴 데이터가 출력된다
# utf8 로 기본적으로 해보고 만약 파일 열었을 때 한글 깨지면 utf-8-sig로 해주면 된다
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# split("\t") tab으로 구분해서 위 title속 문자들이 list로 들어가게 된다
# ["N", "종목명", "현재가"....]
writer.writerow(title)
# list 형태로 제일 첫번째 줄에 구분명들 입력 먼저 하기

for page in range(1, 5):  # 1-4page
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class": "type_2"}).find(
        "tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:
            continue  # 의미 없는 데이터는 스킵
        data = [column.get_text().strip() for column in columns]  # 한 줄 for문
        # 위 strip() 함수를 통해 불필요한 공백들 처리 가능 예.'\n\n\t\t\t\t150\n\t\t\t\t\n' 이런 부분들.
        # print(data[0:-1])  # 끝에 '' 쓸데없는 거 하나 남아서 슬라이싱
        writer.writerow(data[0:-1])
        # 리스트 형태로 데이터 넣고 출력
