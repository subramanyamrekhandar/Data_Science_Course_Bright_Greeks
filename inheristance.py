class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("subclass must implement this method")
class Dog(Animal):
    def speak(self):
        return f"{self.name} in USA"
class Cat(Animal):
    def speak(self):
        return f"{self.name} in UK"
        
        
dog = Dog("shiva")
cat = Cat("subbu")

print(dog.speak())
print(cat.speak())