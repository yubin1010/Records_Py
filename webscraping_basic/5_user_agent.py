# 403 으로 뜰 경우 -> user agent를 잘못 인식하여 응답이 403일 수 있음
import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
res=requests.get(url,headers=headers) # 해당 URL에 요청하여 정보 받아오기
res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)