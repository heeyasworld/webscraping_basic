import requests
res = requests.get("http://google.com")  # url 가져오기
res.raise_for_status()
# 웹스크래핑을 위한 url이 올바르면 그대로 진행
# 아닐 경우에는 오류나고 진행 불가한 코드
# print("status code :", res.status_code)  # 200이면 정상

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
# mygoogle.html이라는 파일을 "w" 쓰기모드로 생성. utf8 넣었으니 한국어지원.
# as f <- f라고 이름 붙이겠다
# 그래서 f.write <- 라고 쓸 수 있다
# f.write(res.text) 즉 google.com의 html 파일을 그대로 받아서 파일화
