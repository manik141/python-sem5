# Program for a number guessing gamne.
from random import randint
def num_gessing():
    secret_number = randint(1,10)
    user_number = int(input("Guess the number: "))
    if secret_number==user_number:
        print("Congratulations! You guessed it right",)
        return -1
    elif secret_number<user_number:
        print("Number too large")
        return 1
    else:
        print("Number too small")
        return 1

while(True):
    print("****MENU****")
    print(" 1 -> Play Game")
    print(" 0 -> Exit")
    choice= int(input("Enter your choice: "))
    if(choice==1):
        cont=num_gessing()
        if(cont==-1):
            break
    elif (choice==0):
        print("*****Exit Game*****")
        break
    else:
        print("Invalid choice! Exit program")
        break