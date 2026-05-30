import random
import time
for i in range(10):
    print("-",end="")
print("\n")
print("HANG-MAN")
print("\n")
for i in range(10):
    print("-",end="")
print("\n")
lifes=5
print("You have five lives left ❤️")
for i in range(lifes):
    print("❤️",end=" ")
print("\n")
file=open("words.txt","r")
s=file.read()
words=s.split(",")
print("Loading word...")
time.sleep(3)
x=random.choice(words)
start_time=time.time()
print("Computer is ready with your word!!")
print(f"It is a {len(x)} letter word")
for i in range(len(x)):
    print("_",end=" ")
print("\n")
j=1
found=0
w=list()
for i in range(len(x)):
    w.append("_")
while lifes>0 and found<len(x):
    print(f"Guess count: {j}")
    guess=input("Enter your guess:")
    if guess in x:
        if guess in w:
            print("you have already guessed the word!!")
            continue
        found=found+x.count(guess)
        print("WOW it is a correct guess 😀!!!")
        l=list()
        for i in range(len(x)):
            if x[i]==guess:
                w[i]=guess
        for p in w:
            print(f" {p}",end="")
        print("\n")
    else:
        print("Oh no you have guessed wrong")
        lifes=lifes-1
        for i in range(lifes):
            print("❤️",end=" ")
        print("\n")
    j=j+1
if found==len(x):
    print(f"Congrats you have won the game, the word was: {x}🤩")
else:
    print(f"Sorry you have lost the correct word was: {x}")
    print("Don't worry try again 🙃")

