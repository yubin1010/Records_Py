#한줄 for
#출석 번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101,102,103,104..
#student = [1,2,3,4,5]
#print(student)
#student = [i+100 for i in student]
#print(student)

#학생 이름을 길이로 변환
#students = ["iron man","thor","groot"]
#students = [len(i) for i in students]
#i는 students에 있는 값들을 하나씩 반복
#print(students)

students = ["iron man","thor","groot"]
students = [k.upper() for k in students]
print(students)