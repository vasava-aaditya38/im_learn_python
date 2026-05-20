a=int(input("enter your age: "))

# if,elif,else ledder

if(a>18):

    print("you are valid")           #"indent"

elif(a<0):
    print("you are entering nagtive invalid age")          
    print("please enter valid age")

elif(a==0):
    print("this is not possible")
    print("'please enter your real age'")

else:
    print("'you are not valid'")          #"indent"

print("end of program")