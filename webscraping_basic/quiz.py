'''
부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오

[조회조건]
1. http://daum.net 접속
2. '송파 헬리오시티' 검색
3. 다음 부동산 부분에 나오는 결과 정보

[출력 결과]
======= 매물 1 =======
거래: 매매
면적: 84/59 (공급/전용)
가격: 165,000(만원)
동: 214동
층: 고/23
======= 매물 2 ======
...

[주의]
실습시점에 위 매물이 없으면 다른 곳으로 대체
'''

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
import time

options = webdriver.ChromeOptions()
options.headless =True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = "http://daum.net"
browser.get(url)

browser.find_element_by_id("q").send_keys("브라운스톤 돈암")
browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]").click()
browser.find_element_by_xpath("//*[@id='estateColl']/div[2]/div/div[2]/div[1]/a").click()

last_tab = browser.window_handles[-1]
browser.switch_to.window(window_name=last_tab)

next_url = browser.current_url+"/items?business=da_www&mkt_source=&service_type=입주2년후"
browser.get(next_url)

time.sleep(5)
res = requests.get(next_url)
print(res.raise_for_status())
soup = BeautifulSoup(browser.page_source, "lxml")

buildings = soup.find_all("div", attrs={"class":"css-1dbjc4n r-14lw9ot r-eqz5dr"})

i=1 
k=0
for building in buildings:
     print("====== 매물 {0} =====".format(i))
     #price = soup.find_all("div", attrs={"class":"css-1dbjc4n r-13awgt0 r-eqz5dr r-1777fci","class":"css-1563yu1"})#.find("div",attrs={"class":"css-1563yu1"}).get_text()
     info = soup.select("div.css-1563yu1")

     att=info[11+i+k].text.split()
     price=" ".join(att[1:])
     att2=info[12+i+k].text.split()
     att3=att2[0].split("·")
     ho=att2[-1]
     dong=att3[1]
     area=att3[0]
     
     print("거래: ",att[0])
     print("가격: ",price)
     print("면적: ",area)
     print("동: ",dong)
     print("호: ",ho)
        
     i+=1
     k+=2