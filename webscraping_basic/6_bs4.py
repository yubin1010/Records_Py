import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a) # 첫번째로 발견되는 a
#print(soup.a.attrs) # a element의 속성 정보
#print(soup.a["href"]) # a element의 href 속성 '값' 정보

#print(soup.find("a", attrs={"class":"Nbtn_upload"})) # a elment의 class가 Nbtn_upload인 처음으로 발견된 속성 값 정보
#print(soup.find(attrs={"class":"Nbtn_upload"})) # 웹툰 올리기 버튼이 하나이기 때문에 a 생략 가능, class=Nbtn_upload인 어떤 element를 찾아줘
#print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs = {"class":"rank01"})
#print(rank1.a.get_text()) # a element만 나오도록
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
#rank2 = rank3.previous_sibling.previous_sibling
#print(rank2.a.get_text())
#print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

all_rank = rank1.find_next_siblings("li") #다음 형제들 모두

i = 1
for rank in all_rank:
    print(str(i),"위 ",rank.a.get_text())
    i+=1

#webtoon = soup.find("a",text="광마회귀-22화")
#print(webtoon)