import random

print("=== Number Guessing Game ===")

num=random.randint(1,100)
a=-1
gueses=0

while(a!=num):
    a=int(input("Chose The number between 1 to 100: "))

    if(a>num):
        print("Chose the lower number")

    elif(a<num):
        print("Chose the Higher number")

    gueses+=1

else:
    print(f"'You chose correct number in ({gueses}) attempt!'")
