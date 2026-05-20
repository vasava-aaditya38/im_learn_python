n: int = 5
name: str="aaditya"

print(n)
print(name)



def sum(a:int ,b:int)->int:
    return a+b

a=sum(3,4)
print(a)

# Handbook Example

def greeting(name:str)->str:
    return f"hello,{name}"

print(greeting("aaditya"))