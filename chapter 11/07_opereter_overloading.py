class number:
    def __init__(self,n):
        self.n=n

    def __add__(self, num):
        return self.n + num.n

a=number(17)
b=number(34)

print(a + b)

# Subtraction

class subtraction:
    def __init__(self,s):
        self.s=s

    def __sub__(self, sub):
        return self.s - sub.s
    
b=subtraction(71)
c=subtraction(10)

print(b - c)

# Multiplaction

class multi:
    def __init__(self,m):
        self.m = m

    def __mul__(self, mul):
        return self.m * mul.m
    
d= multi(5)
e= multi(4)

print(d*e)

# Divison

class div:
    def __init__(self,d):
        self.d=d
    
    def __truediv__(self, di):
        return self.d / di.d
    
f=div(20)
g=div(4)

print(f/g)
