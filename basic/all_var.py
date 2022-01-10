gun = 10

def checkpoint(soldiers):
    global gun #전역 공간에 있은 gun 사용
    #gun = 20
    gun = gun - soldiers
    print("[함수내] 남은 총: {0}".format(gun))

def checkpoint_ret(gun, soldiers): #외부에서 gun을 전달
    gun = gun - soldiers
    print("[함수내] 남은 총: {0}".format(gun))
    return gun #변경된 값 return

print("전체 총: {0}".format(gun))
#checkpoint(2)
gun = checkpoint_ret(gun,2)
print("남은 총:{0}".format(gun))