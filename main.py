import random
n = random.randint(1,100)
a = -1
guesses = 1
while(a !=n):
    guesses +=1
    a = int(input("Guess the number: "))
    if( a>n):
        print("Lower number please")
    elif(a<n):
        print("Higher number please")
        guesses +=1

print(f"You have guessed the number {n} in {guesses} attempt")
