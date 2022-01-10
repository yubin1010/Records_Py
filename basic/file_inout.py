#score_file = open("score.txt","w", encoding="utf-8") #쓰기 위한 목적
#print("수학 : 0", file=score_file)
#print("영어 : 50", file=score_file)
#score_file.close()

#score_file=open("score.txt","a", encoding="utf-8") #append
#score_file.write("과학 : 80")
#score_file.write("\n코딩: 100")
#score_file.close()

#score_file = open("score.txt", "r", encoding="utf-8")
#print(score_file.read())
#score_file.close()

#score_file=open("score.txt","r",encoding="utf-8")
#print(score_file.readline(),end="") # 줄별로 읽기ㅡ 한줄 읽고 커서는 다음 줄로 이동
#print(score_file.readline())
#print(score_file.readline())
#print(score_file.readline())
#score_file.close()

#score_file=open("score.txt","r",encoding="utf-8")
#while True:
#    line = score_file.readline()
#    if not line:
#        break
#    print(line,end="")
#score_file.close()

score_file=open("score.txt","r", encoding="utf-8")
lines = score_file.readlines() # list 형태로 저장
print(type(lines))
for line in lines:
    print(line,end="")
score_file.close()