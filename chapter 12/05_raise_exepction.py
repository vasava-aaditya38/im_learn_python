# Handbook Example

a=int(input("Enter the first value: "))
b=int(input("Enter the second value: "))

if(b==0):
    raise ZeroDivisionError("You cannot divide by zero")
else:
    print(f"The divison of a/b is {a/b}")

# myself

try:
    c=int(input("Enter the number: "))
    d=int(input("Enter the number: "))

    result= c/d

except ZeroDivisionError as z:
    print("You cannot divide by zero")

except ValueError as v:
    print("Enter valid number")

else:
    print(f"The divison of a/b is {result}")

print("End the program!")