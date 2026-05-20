class cacultor:
    
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"The squre of 8 is: {self.n*self.n}")

    def cube(self):
        print(f"The cube of 8 is: {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot of 8 is: {self.n**1/2}")

c=cacultor(8)

c.square()
c.cube()
c.squareroot()