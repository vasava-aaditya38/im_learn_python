
with open("log.txt") as f:
    content= f.read()

if("python" in content):
    print("yes,word is present")

else:
    print("no,word in not present")