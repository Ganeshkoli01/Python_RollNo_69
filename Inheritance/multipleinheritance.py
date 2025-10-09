class A:
       name1="My name is A"
       
class B:
       name2="My name is B"   
       
class C(A,B):
       name3="My name is C"
       
g=C()

print(g.name1)
print(g.name2)
print(g.name3)