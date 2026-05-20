'''
factorial(1) = 1
factorial(2) = 1 X 2 
factorial(3) = 1 X 2 X 3
factorial(4) = 1 X 2 X 3 X 4
factorial(5) = 1 X 2 X 3 X 4 X 5
factorial(n) = n* factorial(n-1)

'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n* factorial(n-1)
    
n=int(input("enter the number: "))

print(f"the factorial of this number is:{factorial(n)}")

