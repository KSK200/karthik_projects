import random

number=[11,24,33,45,56,67,68,90,91]

computerchoice=random.choice(number)
print("computer choice=",computerchoice)

userchoice=int(input("Guess the number:"))

attempt=0
while(True):
    if(userchoice<computerchoice):
        attempt=attempt+1
        userchoice=int(input("Your choice is to lower guess another number:"))
    elif(userchoice>computerchoice):
        userchoice=int(input("Your choice is to higher guess another number:"))
        attempt=attempt+1
    else:
        attempt=attempt+1
        print("your guess ",userchoice," is matched with magic number ",computerchoice)
        print("you have guessed the number in ",attempt," attempts!")
        break
    