# Third project

import random
randnumber = random.randint(1,100)
# print(randnumber)

userguess = 0
guesses = 0

while(userguess != randnumber):
    userguess = int(input("enter a number : "))
    guesses +=1
    if (userguess == randnumber):
        print(f"you guess the right number in {guesses} guesses ")
    else:
        if (userguess < randnumber):
            print("you guesses to small number! please guess larger number")
        else:
            print("you guess to larger number! please guess smaller number")

with open ("hiscore.txt",'r') as f:
    hiscore = int(f.read())

if (guesses <hiscore):
    print("you have just broken the high score")
    with open ("hiscore.txt",'w') as f:
        f.write(str(guesses))
