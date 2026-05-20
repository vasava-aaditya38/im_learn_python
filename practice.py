n = int(input("enter the number: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 *i-1), end="")
    print("")

# end the program3

print("program 2") 

n = int(input("enter the number: "))

for i in range(1, n + 1):
    print("*" * i, end="")
    print("")

# end the program

print("program 3") 

n = int(input("enter the number: "))
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n, end="")

    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*", end="")
    print("")

# end the program

print("program 4") 


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


n = int(input("enter the number: "))
print(f"factorial of this number is:{factorial(n)}")

# end the program

print("program 5") 


def f_to_c(f):
    return 5 * (f - 32) / 9


f = int(input("enter the f: "))

c = f_to_c(f)

print(f"{round(c,2)} degree")

# end the program

print("program 6") 

n=int(input("enter the number: "))

def multiply(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

multiply(n)

# end the program

print("program 7")

def pattern(n):
    if(n==0):
        return 1
    print("*"*n)
    pattern(n-1)

pattern(6)

# end the program

print("program 8") 


def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l=["harrty","rohan","aaditya","an"]

print(rem(l,"an"))

# end the program

print("program 9")

n=int(input("enter the number: "))

for i in range(1,n+1):
    if i==1 or i==n:
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")

# end the program

print("'PROGRAM 10'")

n=int(input("enter the number: "))

for i in range(1,n+1):
    print(" "*(n-1),end="")
    print("*"*(2*i-1),end="")
    print("")

# end the program

print("'program 11'")

n=int(input("enter the number: "))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

# end the program

print("'program 12'")

'''
1 for snake
-1 for water
0 for gun
'''

import random

computer=random.choice([0,1,-1])

youstr=input("enter your choice: ")
youDict={"s":1, "w":-1, "g":0}
reversedDict={1:"snake", -1:"water", 0:"gun"}

you=youDict[youstr]

print(f"your choice is: {reversedDict[you]}\n computer choice is: {reversedDict[computer]}")

if(computer==you):
    print("it's a Draw")

else:
    if(computer==1 and you==-1):
        print("you lose!")

    elif(computer==-1 and you==1):
        print("you Win!")

    elif(computer==1 and you==0):
        print("you Win!")

    elif(computer==0 and you==1):
        print("you Lose!")

    elif(computer==-1 and you==0):
        print("you Lose!")

    elif(computer==0 and you==-1):
        print("you Win!")

    else:
        print("something went wrong")

# End the program

name1=input("enter your name: ")
name2=input("enter your name: ")

def greet(name):
    print("Your Welcome,",name)

greet (name1)
greet(name2)

# End the program

def sum():
    a=int(input("enter the number for sum: "))
    b=int(input("enter the number for sum: "))

    print(f"the sum of this two number is: {a*b}")

sum()

# End the program

password=input("Enter your Password: ")

with open("password.txt","r") as f:
    content=f.read()

if(password in content):
    print("Your Password is in list")
    print("Warning:Change your Password ⚠")

else:
    print("Your password is not in list\nStay alert")

    with open("password.txt","a")as f:
        f.write("\n\n"+password)



# End the program

import random

choice=["rock","paper","sescior"]

you=input("enter your choice[rock,paper,sescior]: ").lower()
computer=random.choice(choice)

print(f"you chose: {you}\ncomputer chose: {computer}")

if(you==computer):
    print("It's tie")

elif(you=="rock" and computer=="paper"):
    print("'You Lose!'")

elif(you=="paper" and computer=="rock"):
    print("You Won!'")
    print("congratulation🎉")

elif(you=="paper" and computer=="sescior"):
    print("'You Lose!'")

elif(you=="sescior" and computer=="paper"):
    print("'You Won!'")
    print("congratulation🎉")

elif(you=="rock" and computer=="sescior"):
    print("'You Won!'")
    print("congratulation🎉")

elif(you=="sescior" and computer=="rock"):
    print("'You Lose!'")

elif(you=="paper" and computer=="sescior"):
    print("'You Lose!'")

elif(you=="sescior" and computer=="paper"):
    print("'You Won!'")
    print("congratulation🎉")

else:
    print("Something went wrong")

# End the program

class carinfo:
    company="Tesla"
    color="White"
    type="Electic"

    def car(self):
        print(f"The car company is: {self.company}\nThe car color is: {self.color}\nThe car type is: {self.type}")

a=carinfo()
a.car()

print("========================")

toyota=carinfo()
toyota.company="Toyota"
toyota.type="Petrol"

toyota.car()

print("========================")

bmw=carinfo()
bmw.company="BMW"
bmw.color="Black"
bmw.type="Disel"

bmw.car()


