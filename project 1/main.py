import random
'''
1 for snake
-1 for water
0 for gun
'''
computer=random.choice([0, 1, -1])
you=input("chose any one [S,W,g]: ").lower()
youDict={"s":1 , "w":-1 , "g": 0}
reversDict={1:"snake" , -1:"water" , 0:"gun"}

you=youDict[you]

print(f"you chose: {reversDict[you]}\ncomputer chose: {reversDict[computer]}")

if(computer==you):
    print("'its a Draw'")

else:
    if(computer==-1 and you==1):
        print("you win!")
        print("congratulation")
    
    elif(computer==1 and you==-1):
        print("you lose!")

    elif(computer==1 and you==0):
        print("you win!")
        print("congratulation")

    elif(computer==0 and you==1):
        print("you lose!")

    elif(computer==0 and you==-1):
        print("you lose!")

    elif(computer==-1 and you==0):
        print("you win!")
        print("congratulation")
    
    else:
        print("something went wrong")
