class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f"The class attribute is: {cls.a}")       # Cls is not compalsury

o=Employee()
o.a=50

o.show()
  

    
