from bs4.element import SoupStrainer
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#네이버 웹툰 전체목록 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"})
# class 속성이 title인 모든 "a" element 반환
i = 1
for cartoon in cartoons:
    print(str(i),cartoon.get_text())
    i+=1