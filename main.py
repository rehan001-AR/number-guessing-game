import random     #import random 
n = random.randint(1,100)  #generate random number between 1 to 100 using random.randint
a = -1  
guesses = 1            #start the guess counter at 1
while(a !=n):          #keep looping until condition is true
    guesses +=1         
    a = int(input("Guess the number: "))   
    if( a>n):              
        print("Lower number please")
    elif(a<n):
        print("Higher number please")       

print(f"You have guessed the number {n} in {guesses} attempt")

