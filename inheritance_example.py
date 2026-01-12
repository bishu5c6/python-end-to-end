# class A:
#     a,b=10,20
#
# class b(A):
#     i, j =1111,22222
#     def m(self,x,y):
#         print(x+y)
#         print(self.i*self.j)
#         print(self.a-self.b)
# o=b()
# o.m(3333,4444)

#oveririding variables
class a:
    name="bishu"
class b(a):
    name ="biswanth"
    def test(self):
        print(super().name())
o=b()
print(o.name)
# o.test()