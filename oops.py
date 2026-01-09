# # we can create a class variable using class keyword
# class myfunc:
#     def cl1(self):
#         print("Hello, this is class1")
#     def cl2(self):
#         print("This is class2")
#
# obj = myfunc()
# obj.cl1()
# obj.cl2()


# we can create a class variable using class keyword
# class myfunc:
#     def cl1(self):
#         print("Hello, this is class1")
#     def cl2(self, name):
#         print(name)
#
# obj = myfunc()
# obj.cl1()
# obj.cl2("Biswanth")

# #creating a program using instance and static method.
# class myclass:
#     def class1(self):
#         print("this is an instance method")
#
#     @staticmethod
#     def cls2(self,name):
#         print(f"This method name is: {name}")
#
# o = myclass()
# o.class1()
# o.cls2("static method","biswanth")
# myclass.cls2("tstauc","biswanth")

#whenever you rae using the static method self also expecting one method



#Example 3
#class variables
#variables which are declared after the class variables is calle class variable
#we can revoke them by using self.a

# class variables:
#     a, b=10, 20 #class variables
#     def mul(self):
#         print(self.a+self.b)
#     def add(self):
#         print(self.a*self.b)
#
# a=variables()
# a.mul()
# a.add()


#example 4 local and global variables
# i, j =15,25
# class var:
#     a,b = 10, 20 #class variables
#     def local(self, x, y): #local variables
#         print(x+y)
#         print(self.a+self.b)
#         print(i+j)
# a=var()
# a.local(1,2)



#example -5 when all the variables have same name:
# i, j =15,25
# class var:
#     i,j = 10, 20 #class variables
#     def local(self, i, j): #local variables
#         print(i+j)
#         print(self.i+self.j)
#         print(globals()['i']+globals()['j'])
# a=var()
# a.local(1,2)



#one class have multile object
class name:
    def n(self,a):
        print("my name is: ", a)

obj=   name()
obj.n("bishu")
obj.n("biswanth")
obj.n('pinnika')

















