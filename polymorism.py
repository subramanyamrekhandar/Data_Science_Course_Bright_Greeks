#polymorphism 

class A:
    def X(self):
        print("flying in the sky")
class Y(A):
    def X(self):
        print("i can't fly")
    
# using polymorsim method    
a = A()
y = Y()

for i in (a, y):
    i.X()