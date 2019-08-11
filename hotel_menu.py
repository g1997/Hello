bill=0
total_bill=0
while True:
    print("******************MENU**********************")
    print("\n1.Veg\n2.Non-Veg\n3.Exit")
    ch1=int(input("Enter your choice:\t"))
    print("*********************************************")
    if ch1==1:
        while True:
            print("******************VEG**********************")
            print("\n1.Starters\n2.Main Course\n3.Beverages\n4.Desserts\n5.Back")
            ch2=int(input("Enter your choice:\t"))
            print("*********************************************")
            if ch2==1:
                while True:
                         print("******************STARTERS**********************")
                         print("\n1.Veg Crispy             \t150\
                                \n2.Veg Spring Roll        \t170\
                                \n3.Veg Garlic Bread       \t140\
                                \n4.Show Bill\
                                \n5.Back")
                         ch4=int(input("Enter your choice:\t"))
                         if ch4==1:
                             q=int(input("Enter Quantity: "))
                             bill+=(150*q)
                             print("\nVeg Cripsy Added.Quantity: ",q)
                             print("**********************************************")

                             continue
                         elif ch4==2:
                             q=int(input("Enter Quantity: "))
                             print("\nVeg Spring Roll Added.Quantity: ",q)
                             bill+=(170*q)
                             print("**********************************************")

                             continue
                         elif ch4==3:
                             q=int(input("Enter Quantity: "))
                             print("\nVeg Garlic Bread Added.Quantity: ",q)
                             bill+=(140*q)
                             print("**********************************************")

                             continue
                         elif ch4==4:
                             print("\n\nBill:\t",bill)
                             print("**********************************************")

                             continue
                         elif ch4==5:
                             break
                     
            elif ch2==2:
                 while True:
                         print("******************MAIN COURSE**********************")
                         print("\n1.Jeera Aloo             \t350\
                                \n2.Aloo Mutter            \t370\
                                \n3.Mutter Paneer          \t340\
                                \n4.Show Bill\
                                \n5.Back")
                         ch5=int(input("Enter your choice:\t"))
                         if ch5==1:
                             q=int(input("Enter Quantity: "))
                             bill+=(350*q)
                             print("\nJeera Aloo Added.Quantity: ",q)
                             print("**********************************************")
                             continue
                         elif ch5==2:
                             q=int(input("Enter Quantity: "))
                             bill+=(370*q)
                             print("\nAloo Mutter Added.Quantity: ",q)
                             print("**********************************************")
                             continue
                         elif ch5==3:
                             q=int(input("Enter Quantity: "))
                             bill+=(340*q)
                             print("\n Mutter Paneer Added.Quantity: ",q)
                             print("**********************************************")
                             continue
                         elif ch5==4:
                             print("\n\nBill:\t",bill)
                             print("**********************************************")
                             continue
                         elif ch5==5:
                             break
                     
                
            elif ch2==3:
                while True:
                             print("******************BEVERAGES**********************")
                             print("\n1.Sodas                  \t20\
                                    \n2.Tea                    \t30\
                                    \n3.Coffee                 \t40\
                                    \n4.Show Bill\
                                    \n5.Back")
                             ch6=int(input("Enter your choice:\t"))
                             if ch6==1:
                                 q=int(input("Enter Quantity: "))
                                 bill+=(20*q)
                                 print("Sodas Added.Quantity: ",q)
                                 print("**********************************************")
                                 continue
                             elif ch6==2:
                                 q=int(input("Enter Quantity: "))
                                 print("Tea Added.Quantity: ",q)
                                 bill+=(30*q)
                                 print("**********************************************")
                                 continue
                             elif ch6==3:
                                 q=int(input("Enter Quantity: "))
                                 print("Coffee Added.Quantity: ",q)
                                 bill+=(40*q)
                                 print("**********************************************")
                                 continue
                             elif ch6==4:
                                 print("\n\nBill:\t",bill)
                                 print("**********************************************")
                                 continue
                             elif ch6==5:
                                 break
                
            elif ch2==4:
                while True:
                     print("******************DESSERTS**********************")
                     print("\n1.Dark chocolate Pie             \t130\
                            \n2.Chocolate Brownie              \t140\
                            \n3.Blueberry Cheesecake           \t210\
                            \n4.Show Bill\
                            \n5.Back")
                     ch5=int(input("Enter your choice:\t"))
                     if ch5==1:
                                 q=int(input("Enter Quantity: "))
                                 bill+=(130*q)
                                 print("\nDark chocolate Pie Added.Quantity: ",q)
                                 print("**********************************************")
                                 continue
                     elif ch5==2:
                                 q=int(input("Enter Quantity: "))
                                 bill+=(140*q)
                                 print("\n.Chocolate Brownie Added.Quantity: ",q)
                                 print("**********************************************")
                                 continue
                     elif ch5==3:
                                 q=int(input("Enter Quantity: "))
                                 bill+=(210*q)
                                 print("\n Blueberry Cheesecake Added.Quantity: ",q)
                                 print("**********************************************")
                                 continue
                     elif ch5==4:
                                 print("\n\nBill:\t",bill)
                                 print("**********************************************")
                                 continue
                     elif ch5==5:
                                 break
            elif ch2==5:
                break
                
    elif ch1==2:
        while True:
                print("******************NON-VEG**********************")
                print("\n1.Starters\n2.Main Course\n3.Beverages\n4.Back")
                ch3=int(input("Enter your choice:\t"))
                if ch3==1:
                    while True:
                     print("******************STARTERS**********************")
                     print("\n1.Chilly Chicken     \t250\
                            \n2.Chicken 65         \t270\
                            \n3.Fish Sticks        \t140\
                            \n4.Show Bill\
                            \n5.Back")
                     ch4=int(input("Enter your choice:\t"))
                     if ch4==1:
                         q=int(input("Enter Quantity: "))
                         print("Chilly Chicken Added.Quantity: ",q)
                         bill+=(250*q)
                         print("**********************************************")

                     elif ch4==2:
                          q=int(input("Enter Quantity: "))
                          print("Chicken 65 Added.Quantity: ",q)
                          bill+=(270*q)
                          print("**********************************************")
                          continue
                     elif ch4==3:
                             q=int(input("Enter Quantity: "))
                             print("Fish Sticks Added.Quantity: ",q)
                             bill+=(240*q)
                             print("**********************************************")

                             continue
                     elif ch4==4:
                             print("\n\nBill:\t",bill)
                             print("**********************************************")

                             continue
                     elif ch4==5:
                             break
                     else:
                         print("\n Invalid choice")
                     
            
                elif ch3==2:
                     while True:
                         print("******************MAIN COURSE**********************")
                         print("\n1.Butter Chicken            \t550\
                                \n2.Chicken Biryani           \t570\
                                \n3.Prawns Masala             \t540\
                                \n4.Show Bill\
                                \n5.Back")
                         ch6=int(input("Enter your choice:\t"))
                         if ch6==1:
                             q=int(input("Enter Quantity: "))
                             bill+=(550*q)
                             print("Butter Chicken Added.Quantity: ",q)
                             print("**********************************************")
                             continue
                         elif ch6==2:
                             q=int(input("Enter Quantity: "))
                             print("Chicken Biryani Added.Quantity: ",q)
                             bill+=(570*q)
                             print("**********************************************")
                             continue
                         elif ch6==3:
                             q=int(input("Enter Quantity: "))
                             print("Prawns Masala added.Quantity: ",q)
                             bill+=(540*q)
                             print("**********************************************")
                             continue
                         elif ch6==4:
                             print("\n\nBill:\t",bill)
                             print("**********************************************")
                             continue
                         elif ch6==5:
                             break
                     
                    
                elif ch3==3:
                    while True:
                                 print("******************BEVERAGES**********************")
                                 print("\n1.Sodas                  \t20\
                                        \n2.Tea                    \t30\
                                        \n3.Coffee                 \t40\
                                        \n4.Show Bill\
                                        \n5.Back")
                                 ch6=int(input("Enter your choice:\t"))
                                 if ch6==1:
                                     q=int(input("Enter Quantity: "))
                                     bill+=20
                                     print("Sodas Added.Quantity: ",q)
                                     print("**********************************************")
                                     continue
                                 elif ch6==2:
                                     q=int(input("Enter Quantity: "))
                                     print("Tea Added.Quantity: ",q)
                                     bill+=(30*q)
                                     print("**********************************************")
                                     continue
                                 elif ch6==3:
                                     q=int(input("Enter Quantity: "))
                                     print("Coffee Added.Quantity: ",q)
                                     bill+=(40*q)
                                     print("**********************************************")
                                     continue
                                 elif ch6==4:
                                     print("\n\nBill:\t",bill)
                                     print("**********************************************")
                                     continue
                                 elif ch6==5:
                                     break
                
                    
                elif ch3==4:
                            break
                else:
                    print("Invalid choice")
                    continue
    elif ch1==3:
        y_n1=input("Do you wish to Exit(y/n)?:")
        if y_n1 in('n','N'):
                continue
        elif y_n1 in('y','Y'):
                     if bill>0:
                         total_bill=bill+(bill*(18/100))
                         print("Thank you,Have a nice day :-),your total bill is: ",total_bill)
                         break
                     else:
                         print("Thank you,Have a nice day :-)")
                         break
        else:   
             print("Invalid choice")
    else:
        print("Invalid Choice")
        continue
                
        

















    













    
