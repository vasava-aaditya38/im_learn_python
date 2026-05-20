f=open('poem.txt')

content=f.read()

if("twinkle" in content):
    print("twinle word is in poem")

else:
    ("twinkle word is in not in poem")

f.close()

# With 

with open("poem.txt") as f:

    content=f.read()

    if("twinkle" in content):
        print("twinkle word is in poem")

    else:
        print("twikle word is not in poem")
