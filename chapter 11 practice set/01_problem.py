class twodvector:
    def __init__(self, i ,j):
        self.i= i
        self.j= j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class threedvector(twodvector):
    def __init__(self,i ,j ,k):
        super().__init__(i, j)          # i Miss parantheses ()
        self.k=k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k ")

a=twodvector(78,45)
a.show()

b=threedvector(45,14,25)
b.show()
