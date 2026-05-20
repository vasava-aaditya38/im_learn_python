with open("players.txt","r") as f:
    content=f.read()

n=input("enter your name: ")

if(n in content):
    print("Your Welcome")
        
else:
    with open("players.txt","a") as f:
        new=f.write(n+"\n\n")

    print(new)

    print("Your Welcome")


 


