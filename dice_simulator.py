#DICE GAME
import random
def p1_turn(p1_moves,p2_moves,trap):
    while True:
        trap=random.randint(5,99)
        print("\n\nPlayer 1s turn.\nPress '1' to roll the dice\n'p' to pass\n'e' to exit: ")
        p1=input("\nEnter your choice:")
        if(p1=='1'):
            d1=random.randint(1,6)
            print("\n\nDice rolled!!!!Number: ",d1)
            p1_moves=p1_moves+d1
            if(p1_moves==trap):
                p1_moves=p1_moves-5
                print("\n\nOOPS!!!!!You entered in trap")
                print("\n\nPlayer1 score: ",p1_moves)
                p2_turn(p1_moves,p2_moves,trap)
            elif(p1_moves==100):
                print("\n\nGame over!!!! Player 1 wins")
                home()
            elif(p1_moves>100):
                p1_moves=p1_moves-d1
                print("\n\nPlayer1 score: ",p1_moves)
                p2_turn(p1_moves,p2_moves,trap)
            else:
                print("\n\nPlayer1 score: ",p1_moves)
                p2_turn(p1_moves,p2_moves,trap)
        elif(p1=='p'):
             p2_turn(p1_moves,p2_moves,trap)
        elif(p1=='e'):
         y_n=input("\n\nDo you wish to exit(y/n)-> ")
         if y_n in('y','Y'):
                print("\n\nGame over!!!!Player 2 wins")
                break
         else:
            continue
        
def p2_turn(p1_moves,p2_moves,trap):
    while True:
        trap=random.randint(5,99)
        print("\n\nPlayer 2s turn.\nPress '2' to roll the dice\n'p' to pass\n'e' to exit: ")
        p2=input("\nEnter your choice: ")
        if(p2=='2'):
            d2=random.randint(1,6)
            p2_moves=p2_moves+d2
            print("Dice rolled!!!!Number: ",d2)
            if(p2_moves==trap):
                p2_moves=p2_moves-5
                print("\n\nOOPS!!!!!You entered in trap, -5 moves deducted\n\n ")
                print("\n\nPlayer 2 score: ",p2_moves)
                p1_turn(p1_moves,p2_moves,trap)
            elif(p2_moves==100):
                print("\n\nGame over!!!! Player 2 wins")
                home()
            elif(p2_moves>100):
                p2_moves=p2_moves-d2
                print("\n\nPlayer2 score: ",p1_moves)
                p1_turn(p1_moves,p2_moves,trap)
            else:
                print("n\nPlayer2 score: ",p2_moves)
                p1_turn(p1_moves,p2_moves,trap)
        elif(p2=='p'):
             p1_turn(p1_moves,p2_moves,trap)
        else:
            y_n=input("\n\nDo you wish to exit(y/n)-> ")
            if y_n in('y','Y'):
                print("\n\nGame over!!!!Player 1 wins")
                home()
            else:
                continue
def home():
    while True:
        p1_moves=0
        p2_moves=0
        trap=0
        print("\n\nWelcome to dice game!!!\nPress 'p' to play\n2.Press 'e' to exit ")
        ch=input("\nEnter your choice:")
        if(ch=='p' or ch=='P'):
                    p1_turn(p1_moves,p2_moves,trap)
        elif(p1=='e'):
                    break
home()
            
