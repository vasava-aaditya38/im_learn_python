# Class is blueprint

class Employee():                      
    language="python"            
    salary=100000 

    def getinfo(self)                     :
        print(f"The employee name is {self.name}.The language is {self.language}.The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

aadi=Employee()
aadi.name="Aadi"            

aadi.greet()
aadi.getinfo()

viren=Employee()
viren.name="viren"
viren.language="Javascirpt"
viren.salary=200000         

viren.greet()
viren.getinfo()

