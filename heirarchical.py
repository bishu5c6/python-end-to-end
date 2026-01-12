class A:
    x,y =10,20
    def m1(self):
        return (self.x+self.y)
class B(A):
    a,b =2,5
    def m2(self):
        return (self.a*self.b)

class C(A):
    c,d = 33,4
    def m3(self):
        print(self.c -self.d)
obj1=C()
obj =B()
obj1.m3()
print(obj.m1())
print(obj.m2())
