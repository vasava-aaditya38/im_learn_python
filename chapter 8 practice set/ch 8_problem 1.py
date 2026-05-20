a= 1
b= 20
c= 37

def gratest(a ,b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
    
print(gratest(a,b,c))