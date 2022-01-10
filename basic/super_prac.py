class Unit:
    def __init__(self, name, hp, speed):#, damage):
        self.name = name # class내에서 정의된 변수 - 멤버변수
        self.hp = hp
        self.speed = speed
        #self.damage = damage
        #print("{0} 유닛이 생성 되었습니다.".format(self.name))
        #print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    def move(self,location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도{2}]" \
            .format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
      #  self.name = name
      #  self.hp = hp
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다.[공격력 {2}" \
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽: 공중 유닛, 수송시. 마린/파이어뱃 / 탱크 등을 수송. 공격 불가
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed=flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도{2}]" \
            .format(name, location, self.flying_speed))

#공중 공격 유닛 - 나는 것, 공격하는것 전부 상속
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0,damage) #지상 스피드 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class BuildingUnit(Unit):
    def __init__(self, name,hp,location):
        Unit.__init__(self, name, hp, 0)
        super().__init__(name,hp, 0) #self 없이 사용
        self.location = location