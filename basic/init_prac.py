#init은 생성자 - 객체 생성
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린",40,5) # self 제외하고 init과 똑같은 객체 개수
marine2 = Unit("마린",40,5)
tank=Unit("탱크",150,35)