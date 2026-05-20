class Employee:
    a=1

class coder(Employee):
    b=2

class Manger(coder):
    c=3

o=Employee()
print(o.a)
# print(o.a,o.b)      # Show an error

c=coder()
print(c.a,c.b)
# print(c.a,c.b,c.c)    # Show an error

m=Manger()
print(m.a,m.b,m.c)