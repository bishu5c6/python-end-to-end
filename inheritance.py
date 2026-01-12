# #single level
# class parent:
#     def m1(self):
#         print("this is parent calss")
#
# class child(parent):
#     def m2(self):
#         print("this is clid class")
#
# a = child()
# a.m2()
# a.m1()
#
#
#
#creating inheritance with class variales.
class A:
    x,y =10,20
    def m1(self):
        return (self.x+self.y)
class B(A):
    a,b =2,5
    def m2(self):
        return (self.a*self.b)

obj =B()
print(obj.m1())
print(obj.m2())


