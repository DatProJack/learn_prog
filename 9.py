import random
updown="Higher"
num=int(random.randint(0,100))
guess=int(raw_input("I have a random number from one to 100. You have 10 tries to guess it. What's your guess: "))
for x in range(1,10):
    if(guess==num):
        print("Great job! You won!")
        break
    else:
        if(guess>num):
            updown="Lower. "
        else:
            updown="Higher. "
        print(updown)
        guess=int(raw_input(" "))
if(guess!=num):
    print("Wow! You really suck at guessing! BTW, the number was ",num)
