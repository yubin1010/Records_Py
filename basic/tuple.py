#리스트와 다르게 내용 변경 및 삭제가 안되지만 속도가 빠름
#변경이 없는 경우만 사용
#리스트는 [] 튜플은()
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스") #오류가 남 추가 및 수정이 불가

#한꺼번에 선언 및 print
name = "김종국"
age = 20 
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)