def open_account():
    print("new account created !")

def deposit(balance, money):
    print("deposit complete. balance {0} won ".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if (balance >= money):
        print("withdraw complete. balance {0} won ".format(balance - money))
        return balance - money
    else:
        print("withdraw fail!. balance {0} won ".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return  commission, balance - money


balance = 0

balance = deposit(balance, 1000)

#balance = withdraw(balance, 500)

commission, balance = withdraw_night(balance, 500)
print("commission is {0} won , balance is {1} won ".format(commission, balance))

