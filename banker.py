import random
from funbank import *
acc={}
while True:
    print("\n1.Create New account\n2.Access Existing account\n3.Exit")
    ch1=int(input("Enter your choice:"))
    if(ch1==1):
        while True:
            ids=input(("\nCreate a username:"))
            ids=ids.lower()
            check=ids in acc.values()
            if check==True:
                print("Username already exists.Try another one")
                y_n=input("Do you want to continue(y/n)?-> ")
                if y_n in('y','Y'):
                    continue
                elif y_n in('n','N'):
                    break
                else:
                    continue
            else:
                pwd=input("\nCreate a password: ")
                acc=collectuser(ids,pwd)
                balance=random.randint(5000,10000)
                print("Account created succcessfully.")
                break
    elif ch1==2:
        while True:
            id1=input(("\nEnter the username:"))
            pwd=input("\nEnter password: ")
            val=validateser(id1,pwd,acc)
            if(val==True):
                print("Login Successful")
                corebank(balance)
                break
            elif(val==False):
                print("\nInvalid username or password")
                y_n=input("Do you want to continue(y/n)?-> ")
                if y_n in('y','Y'):
                    continue
                elif y_n in('n','N'):
                        break
    elif ch1==3:
         y_n=input("Do you wish to exit(y/n)?-> ")
         if y_n in('y','Y'):
            print("Thank you,have a nice day")
            break
         elif y_n in('n','N'):
             continue
         else:
             continue
  
    else:
        print("Invalid choice")
        continue
