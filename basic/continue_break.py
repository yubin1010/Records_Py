absent = [2,5] #결석
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue #스킵하고 다시 반복
    elif student in no_book:
        print("오늘 수업 끝,{0}은 교무실로 와".format(student))
        break #반복값이 있어도 반복문 탈출
    print("{0}, 책을 읽어줘".format(student))