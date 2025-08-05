import random
'''
1 = snake
2 = water
3 = gun

'''
computer = random.choice([1 ,2, 3])
youstr = input("Enter your choice: ")
youdict = {"s" : 1 , "w" : 2 , "g" : 3}
reversedict = {1 : "snake" , 2 : "water" , 3 : "gun"}

try:

    you = youdict[youstr]

    print(f"you chose: {reversedict[you]}\ncomputer chose: {reversedict[computer]}")


    if(computer == you):
        print("Its Draw!")
    else:
        if(computer == 1 and you == 2):
            print("you lose!")

        elif(computer == 1 and you == 3):
            print("you win")
        
        elif(computer == 2 and you == 1):
            print("you win")

        elif(computer == 2 and you == 3):
            print("you win")

        elif(computer == 3 and you == 1):
            print("you lose")

        elif(computer == 3 and you == 2):
            print("you lose")

        else:
            print("somthing went wrong")
except:
    print("you enter a wrong info")
