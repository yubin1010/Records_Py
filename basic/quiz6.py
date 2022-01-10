'''
표준 체중 구하는 프로그램

표준체중: 각 개인의 키에 적당한 체중

남자: 키(m) x 키(m) x 22
여자: 키(m) x 키(m) x 21

1. 표준 체중은 별도 함수 내에서 계산
    함수명: std_weight
    전달값: 키(height), 성별(gender)
2. 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''

def std_weight(height, gender):
    if gender == "남자":
        return height*height*22
    else:
        return height*height*21

height = input("키가 몇이에요? ")
height = int(height)
gender = input("성별이 뭐에요? ")
weight = round(std_weight(height/100, gender),2)

print("키 {0} {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))