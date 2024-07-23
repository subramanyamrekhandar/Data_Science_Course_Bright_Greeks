class Z:
    #initialize or instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #instance methos    
    def X(self):
        return f"{self.name} is {self.age} years old"
    #instance methos   
    def Y(self, location):
        return f"{self.name} in {location} {self.age}"
#attribute classes to creating methods
dog1 = Z("bharath", 3)
dog2 = Z("pavithra", 5)

print(dog1.X())
print(dog2.Y("India"))