word="donkeY"

with open("file.txt") as f:
    content=f.read()

newcontent=content.replace(word,"donkeY")

with open("file.txt","w") as f:
    f.write(newcontent)
