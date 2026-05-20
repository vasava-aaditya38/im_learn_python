# Qution 1

i=1

while i<101:
    print(i)

    i+=1

# Qution 2

i=100

while i>0:
    print(i)
    i-=1

# Qution 3 

n=int(input("Enter the number for table: "))

i=1

while i<11:
    print(f"{n} X {i} = {n*i}")
    i+=1

# Qution 4

nums=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

index=0

while index<10:     #len(nums)= 9
    print(nums[index])      # nums[0], nums[1], nums[2]...
    index+=1

# Qution 5

nums=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

x=36
i=0

while i<len(nums):
    if(nums[i]==x):
        print(f"Eliment ({x}) is exist on index {i} in tuple")

    i+=1

