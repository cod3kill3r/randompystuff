import random
print("A random number guessing game")
num=random.randint(0,10)
print("Enter your guess")
print("Max 3 guesses only")
count=0
while(count<3):
    guess=int(input())
    if guess==num:
        print("You are right")
        break;
    elif(guess<num):
        print("Try guessing the number a bit higher")
        count=count+1
        
    else:
        print("Try guessing the number a bit lower")
        count=count+1
print("The number was: ",num)
print("Thanks for playing")