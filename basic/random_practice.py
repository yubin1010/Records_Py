from random import *

#랜덤 함수 사용
#0.0 ~ 1.0 미만의 임의의 값 생성
print(random())

# 0.0 ~ 10.0. 미만의 임의의 값 생성
print(random() * 10)

#소수점 빼기
print(int(random() * 10 )) # 0 ~ 10 미만의 임의의 값
print(int(random() * 10 )) # 0 ~ 10 미만의 임의의 값
print(int(random() * 10 )) # 0 ~ 10 미만의 임의의 값

#1부터 출력
print(int(random() * 10)+1) # 1 ~ 10 이하의 임의의 값

print(int(random() * 45)+1) # 1~45 이하의 임의의 값 생성

print(randrange(1,46)) # 1~45 이하의 임의의 값 생성

print(randint(1,45)) # 1~45 이하의 임의의 값