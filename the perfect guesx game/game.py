import random
n= random.randint(1,100)
a= -1
guesses= 0
while(a !=n):
    guesses+=1
    a= int(input("Guess the number:"))
    if(a>n):
        print("Guess a lower number")
    else:
        print("Guess a higher number")
    
print(f"You have guessed {n} number in {guesses} guesses")


    