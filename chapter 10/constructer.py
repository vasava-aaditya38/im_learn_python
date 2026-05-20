# Class is blueprint

class Employee():                      
    language="python"            
    salary=100000 

    def __init__(self,name,language,salary):            # It called aurometicly
        self.name=name
        self.language=language
        self.salary=salary

    def getinfo(self)                     :
        print(f"The employee name is {self.name}.The language is {self.language}.The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

aadi=Employee("aadi","java",1000)
print(aadi.name,aadi.language,aadi.salary)

aadi.getinfo()
