n = int(input("enter the number: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1), end="")
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

def multiply(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

multiply(4)

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

print("'program 13'\n ⚠ Qr Code program")

# import qrcode

# url=input("enter the text or url: ")

# img=qrcode.make(url)

# img.save('qrcode.png')

# print("your qrcode is ready")

# End the program

print("'program 14'")

print("Warning: Limit is for 3 person")

people=int(input("How many peoples you are: "))

def guest():
      name=input("Enter your name: ")
      
      with open("guest.txt","a") as f:
            f.write(name+"\n\n")
            
if(people==3):
      guest()
      guest()
      guest()
      
      print("")
      print("Your Entry is Complete!")
      
      with open("guest.txt","a") as f:
            f.write("'Your Most Welcome'"+"\n\n")
      
elif(people<3)     :
      print("Limit is for 3 person")
else:
      print("Limit is for only 3 person")

# End the program

print("'program 15'")

n=int(input("enter the number: "))

factorial=1

if(n<0):
    print("Factorial is does not exist for nagative number")

for i in range(1,n+1):
    factorial*=i

print(f"Factorial of {n} is: {factorial}")

# End the program

print("'program 16")

def add_patient():
    print("\n==Reception==")

    name=input("what is patient name: ")
    age=input("Enter your age: ")
    mobile_no=input("Enter your mobile no: ")
    health_issue=input("Enter your heath issue: ")

    
    with open("patient.txt","a") as f:
         f.write(f"patient name: {name}\n")
         f.write(f"patient age: {age}\n")
         f.write(f"mobile no: {mobile_no}\n")
         f.write(f"patient health issue: {health_issue}\n")
         f.write("--------------------------------\n")
       
        
    print("Appoinment send succesfully")

def view_patient():
    print("'No Patient record found'")

    try:
        with open("patient.txt","r") as f:
            data=f.read()
            print(data)

    except FileNotFoundError:
        print("No patient record found!")

while True:
    print("\n1. Add patient")
    print("2. patient info")
    print("3. Exit")

    choice=input("Enter your choice [1,2,3]: ")

    if(choice=="1"):
        add_patient()

    elif(choice=="2"):
        view_patient()

    elif(choice=="3"):
        print("'Thank you'")
        break

    else:
        print("something went wrong")


