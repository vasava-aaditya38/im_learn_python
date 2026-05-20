marks1=int(input("enter your mark 1: "))
marks2=int(input("enter your mark 2: "))
marks3=int(input("enter your mark 3: "))

total_marks=(100*(marks1 + marks2 + marks3))/300

if(total_marks>40 and marks1>33 and marks2 and marks3):
    print("you are passed",total_marks)
    print("weldone ' keep it up'")

else:
    print("you are failed try again in next year",total_marks)