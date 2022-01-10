import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe") # 같은 경로에 있으면 비워도 됨

# 네이버로 이동
browser.get("http://naver.com")

# 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)
# id를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# html 정보 출력
print(browser.page_source)

# 브라우저 종료
#browser.close() # 현재탭만 종료
browser.quit() # 전체 종료