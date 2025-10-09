# Method Overriding

class Person:
    def show(self):
        print("I am a person")

class Employee(Person):
    
    def show(self):
        print("I am an employee")

p = Person()
e = Employee()

p.show()  
e.show()  




# Method Overloading

class MathOperations:
    def add(self, a=0, b=0, c=0):
        return a + b + c

obj = MathOperations()

print(obj.add(5, 10))     
print(obj.add(2, 3, 4))    
print(obj.add(7))          
