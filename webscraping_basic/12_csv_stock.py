import csv
from os import write
import requests
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="
filename = "시가총액1-200.csv"
f = open(filename,"w",encoding="utf-8-sig",newline="") #newline이 없으면 한줄 띄고 한줄 한줄 띄고 한줄 나옴
writer = csv.writer(f)

title="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
#["N", "종목명","현재가",...]
print(type(title))
writer.writerow(title)

for page in range(1,2):
    res = requests.get(url+str(page),headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    data_rows=soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <=1: #의미 없는 데이터 skip
            continue
        data = [column.get_text().strip() for column in columns] #strip() 공백 제거
        #print(data)
        writer.writerow(data) #wrtierrow 의 list 형태로