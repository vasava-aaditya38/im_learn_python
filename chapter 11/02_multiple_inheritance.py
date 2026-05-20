class Employee:
    name="Aditya"
    company="Goggle"

    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}.")

class coder:
    lang="Python"
    def language(self):
        print(f"Out of all languages he is good in {self.lang}.")

class Programmer(Employee,coder):
    company2 = "ITC Infotech"       # Inheritace 
    def showLanguage(self):
        print(f"The name is {self.name} and the company is {self.company2}.The language is {self.lang}.")


a = Employee()
b = Programmer()

b.show()
b.language()
b.showLanguage()