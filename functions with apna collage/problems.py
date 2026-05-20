# # Problem 1

# cities=["vadodara","ahemdabad","delhi","mumbai"]
# heros=["ironman","thor","spiderman"]
# def lenth():
#     print(len(cities))
#     print(len(heros))

# lenth()


# Problem 2


def fect(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
 
    print(factorial)

fect(5)

# Problem 3

def converter(usd_val):
    inr_val=usd_val*93.63       # 31/3/2026
    print(usd_val, "USD =",inr_val,"INR")
    
converter(2)

# Problem 4

n=int(input("Enter the number: "))

def check():
    if(n%2==0):
        print("Even number!")

    else:
        print("Odd number!")

check()