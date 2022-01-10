#print("Python", "Java", sep=",") #sep를 통해 뭘 할지 선택
#print("Python", "Java", sep=" vs ")

#print("Python", "Java", sep=",", end="?") #end 부분을 통해 한줄에 - 문장의 끝부분을 ?로 바꿔달라, 기존에는 무조건 줄바꿈 
#print("무엇이 더 재밌을까요?")

#import sys
#print("Phyton","Java", file=sys.stdout) # 표준 출력
#print("Phyton","Java", file=sys.stderr) # 표준 에러

#scroes = {"수학":0,"영어":50, "코딩":100}
#for subject, score in scroes.items():
#    #print(subject, score)
 #   print(subject.ljust(8), str(score).rjust(4), sep = ":") #ljust, rjust 공간을 확보하고 왼쪽 오른쪽 정렬

#은행 대기 순번표
#for num in range(1,21):
#    print("대기번호:" + str(num).zfill(3)) #공간을 확보 확보한 빈 공간은 0으로 채움

#answer= input("아무 값이나 입력 : ")
answer = 10
print(type(answer))
#print("입력하신 값은 " +answer)

# input으로 값을 받았을 경우 무조건 type string