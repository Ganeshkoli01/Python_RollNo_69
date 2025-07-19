class A:
          def gk(self):
              print ("hi im A")
              

class B(A):
          def rk(self):
              print ("im chiled of A")
              
              
class C(B):
          print("im chiled of B")
          
g=C()
g.gk()
g.rk()
