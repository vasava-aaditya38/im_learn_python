a=int(input("enter your age: "))

# if statment 1


if(a%2==0):
    print("number is even")

#if statment 2

if(a>18):

    print("you are valid")           #"indent"

elif(a<0):
    print("you are entering nagtive invalid age")          
    print("please enter valid age")

else:
    print("'you are not valid'")          #"indent"

print("end of program")