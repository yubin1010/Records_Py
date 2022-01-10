'''
당신은 cocoa 서비스를 이용하는 택시 기사
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램 작성

1. 승객별 운행 소요시간은 5-50분 사이 난수
2. 당신은 소요 시간 5-15분 사이 승객만 매칭

(출력문 예제)
[0] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[0] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분
'''
'''
from random import *
cnt = 0 #총 탑승 승객
for customer in range(1,51):
    time = int((random() * 50)+1)
    if 5<=time<= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(customer,time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer,time))
print("총 탑승 승객 : {0}분".format(cnt))
'''

from random import *
cnt = 0 
for i in range(1,51):
    time = randrange(5,51)
    if 5<=time<= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
print("총 탑승 승객 : {0}분".format(cnt))
