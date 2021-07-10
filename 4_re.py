import re
# 정규식 라이브러리 가져다 쓸 수 있다

p = re.compile("ca.e")
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
# ^ (^de) : 문자열의 시작 > desk, destination (o) | fade (x)
# $ (se$) : 문자열의 끝 > case, base (o) | face (x)


def print_match(m):
    if m:
        print(m.group(), "매칭")
    else:
        print("매칭되지 않았음")


m = p.match("careless")  # match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)
