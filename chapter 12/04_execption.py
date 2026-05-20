try:
    n=int(input("Enter the number: "))
    print(n)

except ValueError as v:
    print(v)
    print("You type something wrong!")

print("End the program!")