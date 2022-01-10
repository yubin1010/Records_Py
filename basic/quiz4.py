'''
당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석율을 높이기 위해 댓글 이벤트를 진행
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피쿠폰
추첨 프로그램 작성

1. 편의상 댓글은 20명 작성, 아이디는 1~20
2. 댓글 내용과 상관 없이 무작위로 추첨, 중복 불가
3. random 모듈의 shuffle과 sample 활용

(예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
-- 축하합니다 --

(활용예제)
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1)) # 1개를 뽑는 것

'''

from random import *
#lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lst = range(1,21)
lst = list(lst)
shuffle(lst)
#print(lst)
print("-- 당첨자 발표 --")
# 중복이 안되기 때문에 4명을 한번에
winners = sample(lst,4)

print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")

