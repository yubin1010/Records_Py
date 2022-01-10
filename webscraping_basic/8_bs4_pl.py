import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=753853"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[1].a.get_text()
# link = cartoons[0].a["href"]
# print(link)
# print(title)

# for cartoon in cartoons :
#      #title = cartoons[i].a.get_text()
#      title = cartoon.a.get_text()
#      #link = cartoons[i].a["href"]
#      link = cartoon.a["href"]
#      start = 
#      print("https://comic.naver.com"+link)
#      print(title)

#평점 구하기
total_rate=0
cartoons = soup.find_all("div",attrs={"class":"rating_type"})
#star = cartoons[0].strong.get_text()
#print(star)

for cartoon in cartoons:
    rate = cartoon.strong.get_text()
    print(rate)
    total_rate += float(rate)

print("전체", total_rate)
print("평균", total_rate / len(cartoons))
