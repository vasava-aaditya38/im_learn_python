class programer:
    company="Microsoft"

    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language

P=programer("Aadi",100000,"python")
print(P.name,P.salary,P.language,P.company)