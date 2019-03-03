import time #will be using a this module to invoke sleep() function, to introduce delay
score=0
print("Hello there\nLets play a game\nShall we?")
time.sleep(3)
print("\nOkay\nHere we go")
time.sleep(5)
print("\n1.Who is the chief minister of Karnataka?\n")
print("A - H.D. Kumaraswamy\nB - Siddaramaiah\nC - B S Yediyurappa\nD - D K Shivakumar\n")
option=input("Select your option\n")
option=option.upper()
if option=="A":
    print("Correct")
    score=score+10
else:
    print("Wrong Answer, Better luck next time")
    score=score-5;
print("\nNext question")
time.sleep(5)
print("\n2.Who is the CEO of twitter?\nA - Sergey Brin\nB - Paul Allen\nC - Jack Dorsey\nD - Larry Page\n")
option=input("Select your option\n")
option=option.upper()
if option=="C":
    print("Correct")
    score=score+10
else:
    print("Wrong Answer, Better luck next time")
    score=score-5
print("\nNext question")
time.sleep(5)
print("\n3.Who has won the highest number of Formula 1 Championships\nA - Ayrton Senna\nB - Michael Schumacher\nC - Niki Lauda\nD - Fernando Alonso\n")
option=input("Select your option\n")
option=option.upper()
if option=="B":
    print("Correct")
    score=score+10
else:
    print("Wrong Answer")
    score=score-5
print("Calculating scores, please wait......")
time.sleep(5)
print("Your Final Score is :", score)
time.sleep(2)
print("Thanks for playing")
