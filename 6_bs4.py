import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a element를 출력
# print(soup.a.attrs) # a element의 attributes 속성 정보를 dictionary 형태로 보여준다
# print(soup.a["href"])  # a element의 href 속성 '값' 정보를 출력

# print(soup.find("a", attrs={"class": "Nbtn_upload"}).get_text())
# # class="Nbtn_upload"인 a element를 찾아서 text만 출력해줘
# print(soup.find(attrs={"class": "Nbtn_upload"}).get_text())
# class="Nbtn_upload"인 어떤 element를 찾아서 text만 출력해줘

# print(soup.find("li", attrs={"class": "rank01"}).get_text())
rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# # find_next_sibling("li") 라고 하면 중간에 개행이 있더라도
# # next_sibling을 굳이 두 번 넣을 필요없이 다음 "li"를 알아서 찾아준다
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())


total_rank = rank1.find_next_siblings("li")
# siblings <-- 복수형으로 하면 모든 sibling 정보들을 가져옴
print("1", rank1.a.get_text())
a = 1
for i in total_rank:
    a = a + 1
    print(a, i.a.get_text())

# webtoon = soup.find("a", text="이번 생도 잘 부탁해-52화")
# print(webtoon)
