'''
웹 스크래핑을 이용하여 나만의 비서를 만드시오

[조건]
1. 네이버에서 오늘 서울의 날씨 정보를 가져온다
2. 헤드라인 뉴스 3건을 가져온다
3. IT 뉴스 3건
4. 해커스 어학원 홈페이지에서 오늘의 영어 회화 작문

[출력예시]

[오늘의 날씨]
흐림, 어제보다 00도 높아요
현재 00도 (최저 00/최고 00)
강수확률 00%

미세먼지 00 좋음
초미세먼지 00 좋음

[헤드라인 뉴스]
1. 무슨 무슨 일이...
(링크 : https://...)

[IT 뉴스]
1. 무슨무슨 일이
(링크 : https://...)

[오늘의 영어 회화]
(영어 지문)
Jason: how do you think bla bla..?
kim: well, I think ...

(한글 지문)
Json: ...
Kim: ...

'''

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

def weather():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8"
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

   # weather_stat = soup.find("span", attrs={"class":"weather before_slash"}).get_text()
    weather_info = soup.find("div", attrs={"class":"temperature_info"}).get_text().split()
    weather_prev = " ".join(weather_info[:3])
    weather_curr = soup.find("div", attrs={"class":"temperature_text"}).get_text().lstrip()
    weather_low = soup.find("span", attrs={"class":"lowest"}).get_text()
    weather_high = soup.find("span", attrs={"class":"highest"}).get_text()
    print("[오늘의 날씨]")
    print(weather_info[3],",",weather_prev)
    print(weather_curr,"(",weather_low,"/",weather_high,")")
    print(weather_info[4],weather_info[5])

def dust():
    url = "https://weather.naver.com/air/09290580"
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    mise_num = soup.find("span",attrs={"class":"value _cnPm10Value"}).get_text()
    mise_stat = soup.find("span",attrs={"class":"grade _cnPm10Grade"}).get_text()
    chomise_num = soup.find("span",attrs={"class":"value _cnPm25Value"}).get_text()
    chomise_stat=soup.find("span",attrs={"class":"grade _cnPm25Grade"}).get_text()
    print("미세먼지",mise_num,mise_stat)
    print("초미세먼지",chomise_num,chomise_stat)

def news():
    url = "https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    contents = soup.find_all("a",attrs={"class":"list_title nclicks('RBP.rnknws')"})

    print("[헤드라인 뉴스]")
    for i in range(0,3):
        print(i+1,".",contents[i].get_text())
        print("( 링크: ", contents[i]["href"]," )")

def itnews():
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    contents = soup.find("ul",attrs={"class":"type06_headline"}).find_all("li",limit=3)
    print("[IT 뉴스]")
    for index, news in enumerate(contents):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx=1 # img 태그가 있으면 1번쨰 img 태그 정보 사용
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print(index+1,".", title)
        print("(링크: ",link," )")

def english():
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english"
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    print("[오늘의 영어회화]")
    conv = soup.find_all("span",attrs={"class":"conv_sub"})

    #영어 부분
    print("(영어 지문)")
    for i in range(4,8):
        print(conv[i].find("b").get_text())
    print("(한국어 지문)")
    #한국어 부분
    for i in range(0,4):
        print(conv[i].find("b").get_text())

if __name__ == "__main__":
    weather()
    print("\n")
    dust()
    print("\n")
    news()
    print("\n")
    itnews()
    print("\n")
    english()