a=1

while a<=5:
    print("Hello world")
    a+=1

# Reaverse loop

i=5

while i>=1:
    print(i)
    if(i==3):
        break
    i-=1

print("Loop Ended")

print("'only odd numbers'") 

i=0 

while i < 11:
    if(i %2==0):
        i+=1
        continue
    print(i)
    i+=1

print("'only even numbers'") 

i=0

while i<11:
    if(i %2!=0):
        i+=1
        continue
    print(i)
    i+=1