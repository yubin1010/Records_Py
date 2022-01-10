class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # class내에서 정의된 변수 - 멤버변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린",40,5)
marine2 = Unit("마린",40,5)
tank=Unit("탱크",150,35)

#레이스: 공중 유닛, 비행기, 클로킹
wraith1 = Unit("레이스",80,5)
print("유닛이름:{0}, 공격력 {1}".format(wraith1.name, wraith1.damage))#.으로 멤버 변수에 접근 가능

# 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는 것(빼앗음)
wraith2 = Unit("빼앗은 레이스",80,5)
wraith2.clocking = True # 외부에서 클로킹이란 변수를 추가 할당

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))