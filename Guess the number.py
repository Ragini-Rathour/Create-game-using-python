import random

target = random.randint(1,100)

while True:
    userChoice = int(input("Guess the target:"))
    if(userChoice == target):
        print("Success:Correct Guess!!")
        break
    elif(userChoice < target):
        print("your number was too small. Take a bigger guess...")
    else:
        print("your number was too big.Take a smaller guess...")


print("-------GAME OVER-------")
