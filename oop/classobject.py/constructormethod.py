# class Student:
          
#       def __init__(self,name,marks,college):
#           self.name=name
#           self.marks=marks
#           self.college=college
          
          
          
#       def welcome(self):
#           print("gk",self.name)
          
#       def get_marks(self):
#           return self.marks

#       def collegename(self):
#           print("name of college is:",self.college)







# s1=Student("ganesh",98,"DYP")
# #print(s1.name,s1.marks,s1.college)
# s1.welcome()
# print(s1.get_marks())
# s1.collegename()


#Q
class Student():
    
    
    
    
    @staticmethod     #decorator
    def hello():
        print("hello")
        
        
        
        
    def __init__(self,name,phy,che,maths):
        self.name=name 
        self.phy=phy
        self.che=che
        self.maths=maths
        
        
        
        
        
    def get_avr(self):
        print("The average of marks is:",(self.phy+self.che+self.maths)/3)
        
        
        
        
        
name=input("Enter the name of student:")
phy=int(input("Enter the marks of phy:"))
che=int(input("Enter the marks of che:"))
maths=int(input("Enter the marks of maths:"))




gk = Student(name,phy,che,maths)


print("Nmae of student:",gk.name)
print("phy mark is:",gk.phy)
print("che mark is:",gk.che)
print("maths mark is:",gk.maths)
print(gk.get_avr())
print(gk.hello())
