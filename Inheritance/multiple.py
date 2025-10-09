class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called")

class Job:
    def __init__(self, salary):
        self.salary = salary
        print("Job constructor called")

class Employee(Person, Job): 
    def __init__(self, name, salary):
        super().__init__(name)     
        Job.__init__(self, salary)  

    def details(self):
        print(self.name, "earns", self.salary)

emp = Employee("Ganesh koli", 70000)
emp.details()
