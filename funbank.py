import random
def collectuser(ids,pwd):
    acc={"id":ids,"pwd":pwd}
    return acc
def validateser(id1,pwd1,acc):
    if(pwd1 in acc.values() and id1 in acc.values()):
        return True
    else:
        return False
    
def corebank(balance):
    while True:
        print("\n1.Deposit amount\n2.Withdraw amount\n3.Check Balance\n4.Back")
        ch3=int(input("Enter the choice:"))
        if(ch3==1):
            dep=int(input("Enter amount to deposit:\t"))
            balance=balance+dep
            print("Amount deposited!!!!,Balance:",balance)
            continue
        elif ch3==2:
            withdraw=int(input("Enter amount to withdraw:\t"))
            if(balance<=0):
                print("Sorry,You have insufficient Funds!!!!")
                continue
            elif(withdraw>balance):
                print("Withdraw amount is higher than current balance!!!")
                continue
            else:
                balance=balance-withdraw
                print("Amount: ",withdraw,"withdrawn.Current balance:",balance)
        elif ch3==3:
            print("Balance:",balance)
            continue
        elif ch3==4:
            break
        
