class A:
    def __init__(self,a):
        self.vara=a
    def dis(self):
        print(self.vara,"I am Class A")
    def mod(self,a):
        self.vara=a
        
class B:
    def __init__(self,b):
        self.varb=b
    def dis(self):
        print(self.varb,"I am Class B")
    def mod(self,b):
        self.varb=b
        
class C:
    def __init__(self,a,b,c):
        A.__init__(self,a)
        B.__init__(self,b)
        self.varc=c
    def dis(self):
        A.dis(self)
        B.dis(self)
        print(self.varb,"I am Class B")
    def mod(self, a, b, c):
        A.mod(self,a)
        B.mod(self,b)
        self.varc=c

x=C("hi","bye","ty")
x.dis()
x.mod("fy","se","be")
x.dis()

