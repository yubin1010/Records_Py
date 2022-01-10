import requests
res=requests.get("http://google.com") # 해당 URL에 요청하여 정보 받아오기
res.raise_for_status()
#res=requests.get("http://nadocoding.tistory.com")
#print("응답코드 :", res.status_code) # 200이면 정상

#if res.status_code == requests.codes.ok:
 #   print("정상입니다")
#else:
 #   print("문제가 생겼습니다. [에러코드 ",res.status_code, "]")

#res.raise_for_status() #제대로 웹 스크래핑 진행 못할 경우 오류
#print("웹 스크래핑을 진행합니다.")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)
