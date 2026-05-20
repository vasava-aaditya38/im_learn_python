n=int(input("Enter the value: "))

table= [n*i for i in range(1,11)]

with open("table.txt","a")as f:
    f.write(f"Table of {n} is {str(table)}\n\n")
