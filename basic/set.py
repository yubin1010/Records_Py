# 세트 (set)
# 중복이 안되고 순서가 없음 - 집합
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합(java와 python 모두)
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합(java는 할수있지만 python은 못함)
print(java - python)
print(java.difference(python))

#python에 추가
python.add("김태호")
print(python)

#java에서 빠짐
java.remove("김태호")
print(java)