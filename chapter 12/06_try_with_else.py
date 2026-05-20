try:
    n=int(input("Enter the number: "))
    print(n)


except ValueError as v:
    print("Enter integer number!")

else:
    print("im inside else")     # if else print that means try block was run succensfully.