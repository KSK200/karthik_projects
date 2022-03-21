import random

game=["stone","paper","seizer"]
computer_choice=random.choice(game)

print("computer choice from list ",game," is ",computer_choice)
print("\n")
print("Select your choice from list:",game," to play the game")
userchoice=input("user choice:")
cs=0
us=0
if userchoice in game:
    if(computer_choice=="stone" and userchoice=="seizer"):
        print("computer won the game")
    elif(computer_choice=="seizer" and userchoice=="paper"):
        print("computer won the game")
    elif(computer_choice=="paper" and userchoice=="stone"):
        print("computer won the game")
    elif(userchoice=="stone" and computer_choice=="sizer"):
        print("user won the game")
    elif(userchoice=="seizer" and computer_choice=="paper"):
        print("user won the game")
    elif(userchoice=="paper" and computer_choice=="stone"):
        print("user won the game")    
        
print("\n")
