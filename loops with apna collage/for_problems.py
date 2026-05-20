l=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for value in l:
    print(value)


# problem 2

t=(1, 4, 9, 16, 25, 36, 49, 64, 81,100,25)
x=25
idz=0

for value in t:
    if(value==x):
        print(f"The value ({x}) is found at index {idz}")
    idz+=1

#problem 3

for i in range(1,101):
    print(i)

# problem 4

for i in range(100,0,-1):
    print(i)

#problem 5

i=1
n=5
sum=0

while i<=n:
    sum+=i
    i+=1

print(f"Total sum is: {sum}")

# problem 6

n=5
factorial=1

for i in range(1,n+1):
    factorial*=i

print(f"The factorial of {n} is {factorial}")    