import random
computer =random.choice([1,-1,0])               #generates random from 1,-1,0

try:                                                    #for error handling
    youstr =input("Enter s (for Stone) ,p(for paper) , sc(scissors): ")
    youDict ={"s":1,"p":-1,"sc":0}                      #creating Directory
    reverseDict ={1:"stone",-1:"paper",0:"scissor"}     #reverse mapping of directory
    you = youDict[youstr]
except KeyError:
    print("please enter stone or paper or scissor")     #only print when user enter something else

print(f"you choice {reverseDict[you]}\nComputer choice {reverseDict[computer]}")

if(computer==you):
    print(f"you both choice {youstr} match tie")

elif(computer==1 and you==-1):
    print("you win")

elif(computer==1 and you==0):
    print("you loose")

elif(computer==-1 and you==1):
    print("you loose")

elif(computer==-1 and you==1):
    print("you loose")

elif(computer==-1 and you==0):
    print("you win")

elif(computer==0 and you==1):
    print("you win")

elif(computer==0 and you==-1):
    print("you loose")
else:
    print("Something went wrong...")




