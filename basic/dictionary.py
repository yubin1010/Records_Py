#key-value 형, key에대한 중복이 허용되지 않음
#cabinet = {3:"유재석", 100:"김태호"} #3번키에 대해 유재석이 value, 100번키에 대해 김태호
#print(cabinet[3])
#print(cabinet[100])

#print(cabinet.get(3))
#print(cabinet[5]) #오류가 나서 프로그램이 종료
#print(cabinet.get(5)) #None 출력후 프로그램 계속 실행
#print(cabinet.get(5,"사용 가능"))
#print("hi")

#print(3 in cabinet) # 3이라는 key가 cabinet에있는가
#print(5 in cabinet)


#String key
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet.get("A-3"))
print(cabinet["A-3"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 전체 지우기
cabinet.clear()
print(cabinet.items())