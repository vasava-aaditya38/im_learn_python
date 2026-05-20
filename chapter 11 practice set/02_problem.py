class animals:
    pass

class pets(animals):
    pass

class dog(pets):
    @staticmethod
    def bark():
        print("Bow Bow!")
        
a=dog()
a.bark()