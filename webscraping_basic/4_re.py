#주민등록번호 901201-2222222 
#이메일 주소 hello@gmail.com
#차량 번호 232가1234

import re #정규식
#차량 번호판은 4자리 문자라고 가정
#세개만 기억남 (ca?e)

p = re.compile("ca.e") 
# . (ca.e): 하나의 문자를 의미 > care, cafe, case
# ^ (^de): 문자열의 시작 > desk, destination
# $ (se$): 문자열의 끝 > case, base

def print_match(m):
    #m = p.match("case") # case가 매칭이 되어서 출력
    #m = p.match("caffe") # 매치되지 않으면 에러가 발생
    #print(m.group())
    if m:
        print("m.group ", m.group()) # 일치하는 문자열 반환
        print("m.string ", m.string) # 입력 받은 문자열
        print("m.start ", m.start()) # 일치하는 문자열의 시작 index
        print("m.end ",m.end()) # 일치하는 문자열의 끝 index
        print("m.span ",m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭 되지 않음")

#m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인 -> careless는 그래서 매칭 가능
#print_match(m)

m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)

#lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
#print(lst)

'''
1. p = re.compile("원하는 정규식")
2. m = p.match("비교할 문자열")
3. m = p.search("비교할 문자열")
4. lst = p.findall("비교할 문자열")

원하는 형태 : 정규식
 . (ca.e): 하나의 문자를 의미 > care, cafe, case
 ^ (^de): 문자열의 시작 > desk, destination
 $ (se$): 문자열의 끝 > case, base

'''