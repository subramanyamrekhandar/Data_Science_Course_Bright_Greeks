#encapsulation:
class Person:
    def __init__(self, name, age):
        self.__name = name # private data
        self.__age = age #private data
    
    #get method
    def get_name(self):
        return self.__name
    #set methods    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("age must be positive")
    
    #display method
    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")
        
persondetails = Person("shiva", 24)
persondetails.display_info()


print(persondetails.get_name())
#print(persondetails.set_age())
persondetails.set_age(35)
persondetails.display_info()












