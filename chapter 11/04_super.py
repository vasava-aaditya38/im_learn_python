class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1

class coder(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Coder")           # Myself
    b=2

class Manger(coder):
    def __init__(self):
        super().__init__()              # Super method Vs code suggest you
        print("Constructor of Manger")
    c=3

# o=Employee()
# print(o.a)
     
# c=coder()
# print(c.a,c.b)

m=Manger()
print(m.a,m.b,m.c)