'''
함수? box라고 생각
'''

def open_account():
    print("새로운 계좌가 생성되었습니다.")

#open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원".format(balance-money))
        return balance - money
    else:
        print("출금 불가. 잔액은 {0}원".format(balance))

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission #tuple 형식으로 보냄

balance = 0 
balance = deposit(balance, 1000)
#balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원, 잔액은{1}".format(commission, balance))