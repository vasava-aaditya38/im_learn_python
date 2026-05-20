def add_num(a,b):       # parameters
    result=a+b
    return f"{a} + {b} = {result}"

print(add_num(5,4))     # Arugument

print(add_num(100,21))

# Average calucltor

a=int(input("Enter the first value: "))
b=int(input("Enter the second value: "))
c=int(input("Enter the third value: "))

def avarge():
    sum=a+b+c
    avg=sum / 3
    print(avg)

avarge()